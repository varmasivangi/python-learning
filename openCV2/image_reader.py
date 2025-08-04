import cv2 as cv

capture = cv.VideoCapture('openCV2/media/sample.mp4')
def reScaleFrame(frame,scale):
    width = int(frame.shape[1] * scale)
    height =int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)


# for live video
def changeres(width,height):
    capture.set(3,width)
    capture.set(4,height)

    



image = cv.imread('openCV2/media/profile.jpeg',0)
resized_image = reScaleFrame(image,0.5)

cv.imshow('image',image)
cv.imshow('resized image', resized_image)
cv.waitKey(0)
cv.destroyAllWindows()


# capture = cv.VideoCapture('openCV2/media/sample.mp4')

# while True:
#     isTrue, frame = capture.read()
#     if not isTrue:
#         print("Video has ended or file not found.")
#         break

#     cv.imshow('video frame', frame)
#     if cv.waitKey(20) & 0xFF == ord('d'):  # Press 'd' to break
#         break

