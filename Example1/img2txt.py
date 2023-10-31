#!/usr/bin/env python3

# Source: https://builtin.com/data-science/python-ocr

from PIL import Image
import cv2
import pytesseract
import numpy as np

#  ---------
# | Image 1 |
#  ---------

filename1 = "../sample1.jpg"

img1 = np.array(Image.open(filename1))

text1 = pytesseract.image_to_string(img1)
print(f"Result: {text1}")

#  ---------
# | Image 2 |
#  ---------

filename2 = "../sample2.jpg"

img2 = np.array(Image.open(filename2))
cv2norm_img = np.zeros((img2.shape[0], img2.shape[1]))
img2 = cv2.normalize(img2, cv2norm_img, 0, 255, cv2.NORM_MINMAX)
img2 = cv2.threshold(img2, 100, 255, cv2.THRESH_BINARY)[1]
img2 = cv2.GaussianBlur(img2, (1, 1), 0)

text2 = pytesseract.image_to_string(img2)
print(f"Result: {text2}")
