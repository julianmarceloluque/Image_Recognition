import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/cat.jpg')
cv.imshow('Cat',img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Black Image',blank)

print(img.shape)
print(blank.shape)

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('Mask', mask)

print(mask.shape)

masking = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masking', masking)

cv.waitKey(0)