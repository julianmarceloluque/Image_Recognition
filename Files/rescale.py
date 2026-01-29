import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    # Image, Video, Live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)

img = cv.imread('Resources/Photos/cat.jpg')
img_resized = rescaleFrame(img)
capture = cv.VideoCapture(0)

## Change the resolution of the capture (Live video)
#changeRes(100,100)

cv.imshow('Cat', img)
cv.imshow('Cat frame_resized',img_resized)

while True:
    ret, frame = capture.read()
    if not ret:
        print("Can't open the frame. Closing...")
        break

    cv.imshow('Live video camera', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()