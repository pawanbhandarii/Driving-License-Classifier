import cv2
import numpy as np

# Set up the camera capture
frame = cv2.imread("newcircle.png")

# Pre-process the frame to remove noise and improve contrast
frame = cv2.GaussianBlur(frame, (5, 5), 0)
frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Use Hough transform to detect lines in the frame
lines = cv2.HoughLinesP(frame, 1, np.pi/180, 50,
                        minLineLength=50, maxLineGap=10)

# Iterate through the detected lines and draw them on the frame
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

# Use color thresholding to extract the road lines
lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])
mask = cv2.inRange(frame, lower_yellow, upper_yellow)
mask = cv2.bitwise_not(mask)
road_lines = cv2.bitwise_and(frame, frame, mask=mask)

# Display the original frame and the extracted road lines
cv2.imshow("Original", frame)
cv2.imshow("Road Lines", road_lines)



# Release the camera and destroy the windows
cap.release()
cv2.destroyAllWindows()
