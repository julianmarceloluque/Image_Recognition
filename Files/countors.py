import cv2 as cv
import numpy as np

def rescaleFrame(frame, scale=0.75):
    # Image, Video, Live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# 1 - Load Image
img = rescaleFrame(cv.imread('Resources/Photos/HungriaParlament.jpg'), 0.3)
cv.imshow('Image', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank image', blank)

# 2 - Convert to gray scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray image', gray)

# OPTION 1
# 3 - Blur the image
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur image', blur)

# 3 - Detect te edges
canny = cv.Canny(blur, 125,175)
cv.imshow('Canny image', canny)

## OPTION 2
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh Image', thresh)

# 4 - Countours
cannycontours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(cannycontours)} countours(s) found with canny!')

tcontours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(tcontours)} countours(s) found with thresh!')

cv.drawContours(blank, cannycontours, -1, (0,0,255), 1)
cv.imshow('Contours with Canny', blank)

blank[:] = 0

cv.drawContours(blank, tcontours, -1, (0,0,255), 1)
cv.imshow('Contours with Thresh', blank)


cv.waitKey(0)