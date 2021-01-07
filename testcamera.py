import cv2
import numpy as np

def nothing(x):
    pass
path_img = '/Users/Nut_NTCH/Desktop/8.jpg'
img = cv2.imread(path_img)
cv2.namedWindow("HSV_FILTER")
cv2.createTrackbar("h1", "HSV_FILTER", 0, 180, nothing)
cv2.createTrackbar('s1', "HSV_FILTER", 0, 255, nothing)
cv2.createTrackbar("v1", "HSV_FILTER", 0, 255, nothing)
cv2.createTrackbar("h2", "HSV_FILTER", 0, 180, nothing)
cv2.createTrackbar('s2', "HSV_FILTER", 0, 255, nothing)
cv2.createTrackbar("v2", "HSV_FILTER", 0, 255, nothing)

while True:
    frame = cv2.imread(path_img)
    frame = cv2.resize(frame, (400, 300))
    frame = cv2.flip(frame, 1)
    blurred_frame = cv2.GaussianBlur(frame, (5, 5), 1)

    hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

    h1 = cv2.getTrackbarPos("h1", "HSV_FILTER")
    s1 = cv2.getTrackbarPos("s1", "HSV_FILTER")
    v1 = cv2.getTrackbarPos("v1", "HSV_FILTER")
    h2 = cv2.getTrackbarPos("h2", "HSV_FILTER")
    s2 = cv2.getTrackbarPos("s2", "HSV_FILTER")
    v2 = cv2.getTrackbarPos("v2", "HSV_FILTER")

    lower = np.array([h1, s1, v1])
    upper = np.array([h2, s2, v2])
    mask = cv2.inRange(hsv, lower, upper)

    cv2.imshow("Mask", mask)
    cv2.imshow("fram", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()