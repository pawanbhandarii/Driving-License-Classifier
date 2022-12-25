import cv2
import numpy as np

ims = cv2.imread("newcircle.png")
img = cv2.resize(ims, (960, 540))
# pre process the frame ti remove noise and improve contrast
frame = cv2.GaussianBlur(img, (5, 5), 0)
frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_yellow = np.array([58, 95, 45])
upper_yellow = np.array([58, 100, 50])
edges = cv2.Canny(gray, 150, 75)
# use houghtransform to detect lines and draw them
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 5)
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
mask = cv2.bitwise_not(mask)
result = cv2.bitwise_and(img, img, mask=mask)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

#cv2.imshow("edges", edges)
cv2.imshow("Image", img)
# cv2.imshow("yellow",mask)
#cv2.imshow("mask", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
