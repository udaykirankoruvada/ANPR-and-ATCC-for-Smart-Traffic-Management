##import cv2
##import pytesseract
##from PIL import Image
##
##pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
##
##
##
### Load image
##img = cv2.imread('test.jpg')
####img.show()
##
### Convert to grayscale
##gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
##
### Apply thresholding to get a binary image
##_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
##
### Denoising (optional, depending on the image quality)
##denoised = cv2.fastNlMeansDenoising(thresh, None, 30, 7, 21)
##
### Optionally resize the image for better recognition
##resized_img = cv2.resize(denoised, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
##
### Use Tesseract to extract text
##text = pytesseract.image_to_string(resized_img)
##print(text)


import easyocr

# Initialize EasyOCR reader with English language
reader = easyocr.Reader(['en'])

# Read text from the image
result = reader.readtext('path_to_image.jpg')

# Print the result
for detection in result:
    print(detection)
