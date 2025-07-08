import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Resources/Photos/cat.jpg')
cv.imshow('Cat', img)

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Cat', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV Cat', hsv)

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB Cat', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB Cat', rgb)

plt.imshow(rgb)
plt.show()

cv.waitKey(0)