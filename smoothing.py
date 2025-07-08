import cv2 as cv

img = cv.imread('Resources/Photos/cat.jpg')
cv.imshow('Cat',img)

kernel = (3,3)

# Averaging
average = cv.blur(img, kernel)
cv.imshow('Average Blur', average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, kernel, 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral
bilateral = cv.bilateralFilter(img, 70, 50, 40)
cv.imshow('Bilateral Blur', bilateral)


cv.waitKey(0)