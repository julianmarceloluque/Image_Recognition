import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/cat.jpg')
cv.imshow('Cat',img)

# Axiliar Matrix
blank = np.zeros(img.shape[:2], dtype='uint8')

# Split the image
b,g,r = cv.split(img)

cv.imshow('Blue matrix',b)
cv.imshow('Green matrix',g)
cv.imshow('Red matrix',r)
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# Merge the matrix with blank
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])
cv.imshow('Image blue',blue)
cv.imshow('Image green',green)
cv.imshow('Image red',red)

# Reconstruct the original image
merged = cv.merge([b,g,r])
cv.imshow('Image merged',merged)

cv.waitKey(0)