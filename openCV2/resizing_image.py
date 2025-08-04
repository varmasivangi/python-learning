import cv2 as cv

image = cv.imread('openCV2/media/profile.jpeg',-1)
cv.imshow('image',image)



def reScaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)


# cv.waitKey(0)
image_resized = reScaleFrame(image,0.5)
cv.imshow('resized image', image_resized)

capture = cv.VideoCapture('openCV2/media/sample.mp4',0)  # Check the path is correct

while True:
    isTrue, frame = capture.read()

    frame_resized  = reScaleFrame(frame,0.2)
    
    if not isTrue:
        print("Video has ended or file not found.")
        break

    cv.imshow('video frame', frame)
    cv.imshow('resized video frame', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):  # Press 'd' to break
        break

# Move these outside the loop
capture.release()
cv.destroyAllWindows()