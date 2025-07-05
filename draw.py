import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

# 1. Point the image a certain colour
blank[100:200] = 0,255,0 # R / G / B
blank[300:400] = 255,0,0
blank[:,200:300] = 0,0,255
cv.imshow('Draw 1', blank)
blank[:] = 0

# Auxiliar p = (widt,height)
point_0 = (0,0)
point_1 = (100,100)
point_2 = (200,200)

point_3 = (300,100)
point_4 = (400,200)

point_5 = (100,300)
point_6 = (200,400)

# point_ = (300,300)
# point_ = (,)

# Auxiliar color in BGR
bgr_red = (0,0,255)
bgr_blue = (255,0,0)
bgr_green = (0,255,0)

# 2. Draw a rectangle
cv.rectangle(blank, point_1, point_2, bgr_red, thickness=1) # color : B/G/R
cv.rectangle(blank, point_3, point_4, bgr_blue, thickness=cv.FILLED) # color : B/G/R
cv.rectangle(blank, point_5, point_6, bgr_green, thickness=-1) # color : B/G/R
cv.imshow('Draw 2', blank)
blank[:] = 0

# Auxiliar
width_divided = blank.shape[1]//2
height_divided = blank.shape[0]//4
# 2.1 Draw a rectangle proportional
cv.rectangle(blank, point_0, (width_divided,height_divided), bgr_blue, thickness=cv.FILLED)
cv.imshow('Draw 3', blank)
blank[:] = 0

# 3 Draw a circle
cv.circle(blank, point_1, 50, bgr_blue, thickness=3)
cv.imshow('Draw 4', blank)
blank[:] = 0

# 4 Draw a line
cv.line(blank, point_1, point_6, bgr_red, thickness=3)
cv.imshow('Draw 5', blank)
blank[:] = 0

# 5 Draw Text
cv.putText(blank,'Hello World!', (50,255), cv.FONT_HERSHEY_COMPLEX, 2.0, bgr_green, thickness=2)
cv.imshow('Draw 6', blank)

cv.waitKey(0)