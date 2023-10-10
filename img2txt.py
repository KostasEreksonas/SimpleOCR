#!/usr/bin/env python3

from PIL import Image
import pytesseract
import numpy as np

filename1 = "sample1.jpg"
filename2 = "sample2.jpg"

img1 = np.array(Image.open(filename1))
img2 = np.array(Image.open(filename2))
text1 = pytesseract.image_to_string(img1)
text2 = pytesseract.image_to_string(img2)

print(text1)
print(text2)
