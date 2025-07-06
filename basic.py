import cv2 as cv

def rescaleFrame(frame, scale=0.5):
    # Image, Video, Live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = rescaleFrame(cv.imread('Resources/Photos/cat.jpg'))
cv.imshow("Cat", img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray cat', gray)

# Auxiliar Blur
n = 7 # prime number / example: 1, 3, 5, 7, ...
kernel = (n,n)
# Blur
blur = cv.GaussianBlur(img, kernel, cv.BORDER_DEFAULT)
cv.imshow('Blur cat', blur)

# Edge Cascade
canny = cv.Canny(blur, 110, 200)
cv.imshow('Canny', canny)

# Dilating the image
dilated = cv.dilate(canny, kernel, iterations=3)
cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, kernel, iterations=3)
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)