import ast
import cv2
import numpy as np
import pandas as pd

# Load the results CSV
results = pd.read_csv('results/interpolated_main.csv')

# Load video
video_path = 'dataset/videoData/2303099-uhd_2560_1440_30fps.mp4'
cap = cv2.VideoCapture(video_path)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Specify the codec
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

out = cv2.VideoWriter('output/main.mp4', fourcc, fps, (width, height))

# Prepare license plate data
license_plate = {}

for car_id in np.unique(results['car_id']):
    max_score = np.amax(results[results['car_id'] == car_id]['license_number_score'])
    license_plate[car_id] = {
        'car_class': results[(results['car_id'] == car_id) &
                             (results['license_number_score'] == max_score)]['car_class'].iloc[0],
        'license_plate_number': results[(results['car_id'] == car_id) &
                                        (results['license_number_score'] == max_score)]['license_number'].iloc[0]
    }

frame_nmr = -1
cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

# Process video frames
ret = True
while ret:
    ret, frame = cap.read()
    frame_nmr += 1
    if ret:
        df_ = results[results['frame_nmr'] == frame_nmr]
        for row_indx in range(len(df_)):
            # Parse bounding boxes
            car_x1, car_y1, car_x2, car_y2 = ast.literal_eval(
                df_.iloc[row_indx]['car_bbox']
                .replace('[ ', '[').replace('   ', ' ').replace('  ', ' ').replace(' ', ',')
            )

            # Define colors for different car types
            color_dict = {
                "car": (0, 255, 0),
                "bus": (0, 0, 255),
                "truck": (255, 0, 0),
                "motorcycle": (255, 255, 0),
                "0": (0, 255, 255)
            }
            object_class_name = license_plate[df_.iloc[row_indx]['car_id']]['car_class']
            object_color = color_dict.get(object_class_name, (255, 255, 255))  # Default white if class not found

            # Draw car bounding box
            cv2.rectangle(frame, (int(car_x1), int(car_y1)), (int(car_x2), int(car_y2)), object_color, 2)

            # Draw license plate bounding box
            x1, y1, x2, y2 = ast.literal_eval(
                df_.iloc[row_indx]['license_plate_bbox']
                .replace('[ ', '[').replace('   ', ' ').replace('  ', ' ').replace(' ', ',')
            )
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 1)

            # Draw text with a white background
            try:
                # Get the text to display
                text = f"{object_class_name}: {license_plate[df_.iloc[row_indx]['car_id']]['license_plate_number']}"

                # Define font properties
                font = cv2.FONT_HERSHEY_SIMPLEX
                font_scale = 2
                thickness = 2

                # Calculate text size and baseline
                (text_width, text_height), baseline = cv2.getTextSize(text, font, font_scale, thickness)

                # Calculate text position
                text_x, text_y = int(car_x1), int(car_y1) - 5  # Slightly above the bounding box

                # Draw a white rectangle behind the text
                cv2.rectangle(
                    frame,
                    (text_x, text_y - text_height - baseline),
                    (text_x + text_width, text_y + baseline),
                    (255, 255, 255),  # White background
                    thickness=cv2.FILLED
                )

                # Draw the text on top of the rectangle
                cv2.putText(
                    frame,
                    text,
                    (text_x, text_y),
                    font,
                    font_scale,
                    object_color,  # Text color (use object color)
                    thickness
                )
            except Exception as e:
                print(f"Error drawing text: {e}")
                pass

        # Write the frame to the output video
        out.write(frame)

        # Resizing the video and showing the result live
        frame = cv2.resize(frame, (1280, 720))
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

out.release()
cap.release()
cv2.destroyAllWindows()
