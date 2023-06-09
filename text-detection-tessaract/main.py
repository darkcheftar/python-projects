import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"<Path-to-Tessaract>"

img = cv2.imread(r'inputs\1.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

print(pytesseract.image_to_string(img))

cv2.imshow('result', img)
cv2.waitKey(0)