import matplotlib.pyplot as plt

import image_ocr

# image-ocr will automatically download pretrained
# weights for the detector and recognizer.
pipeline = image_ocr.pipeline.Pipeline()

# Specify paths to local images
image_paths = [
    "car2.jpg",
]

# Load images from local paths
images = [image_ocr.tools.read(path) for path in image_paths]
# Each list of predictions in prediction_groups is a list of
# (word, box) tuples.
prediction_groups = pipeline.recognize(images)


# Plot the predictions

# fig, axs = plt.subplots(nrows=len(images), figsize=(20, 20))
for image, predictions in zip(images, prediction_groups):
    # image_ocr.tools.drawAnnotations(image=image, predictions=predictions, ax=ax)
    print(predictions)

#
# import cv2
# from PIL import Image
# import matplotlib.pyplot as plt
# import image_ocr
# import os
#
# # # Preprocessing Function
# # def preprocess_image(image_path):
# #     image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
# #     _, thresh = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# #     kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
# #     processed = cv2.dilate(thresh, kernel, iterations=1)
# #     return processed
# #
# # # Save OpenCV processed image to disk
# # def save_processed_image(cv_image, output_path):
# #     cv2.imwrite(output_path, cv_image)
#
# # Post-processing Function
# def merge_predictions(predictions):
#     # Merge predictions based on horizontal proximity
#     merged = ""
#     for word, _ in sorted(predictions, key=lambda x: x[1][0][0]):  # Sort by x-coordinate
#         merged += word + " "
#     return merged.strip()
#
# # Initialize OCR pipeline
# pipeline = image_ocr.pipeline.Pipeline()
#
# # Specify paths to local images
# image_paths = ["car.jpg"]
# processed_image_paths = []
#
# # # Preprocess images and save them temporarily
# # for idx, path in enumerate(image_paths):
# #     processed_image = preprocess_image(path)
# #     processed_path = f"processed_{idx}.jpg"
# #     save_processed_image(processed_image, processed_path)
# #     processed_image_paths.append(processed_path)
#
# # Run OCR on processed images using file paths
# prediction_groups = pipeline.recognize(image_paths)
#
# # Handle and display results
# for image_path, predictions in zip(processed_image_paths, prediction_groups):
#     # Merge predictions to detect license plate as a single entity
#     license_plate = merge_predictions(predictions)
#     print(f"Detected License Plate from {image_path}: {license_plate}")
#
# # Clean up temporary processed images
# for temp_path in processed_image_paths:
#     os.remove(temp_path)
