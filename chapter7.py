'''
Detekcja koloru dziobu tukana:
1. zmiana przestrzeni kolorow z RGB na HSV
2. wygenerowanie suwaków, którymi reguluje się odcien, jasnosc i nasycenie
3. wybranie koloru do detekcji za pomocą suwaków
4. utworzenie maski i nalozenie jej na obraz
'''

import cv2
import numpy as np
from stack import stackImages


def empty(a): pass

cv2.namedWindow("Trackbar")   # utworzenie okna
cv2.resizeWindow("Trackbar", 650, 250)

cv2.createTrackbar("Hue Min", "Trackbar", 0, 179, empty)  # wykonanie suwaka odcienia(hue) w oknie; 0-179 poziomy koloru w skali HSV
cv2.createTrackbar("Hue Max", "Trackbar", 98, 179, empty)
cv2.createTrackbar("Sat Min", "Trackbar", 139, 255, empty)  # wykonanie suwaka nasycenia(saturation) w oknie; 0-255 poziomy
cv2.createTrackbar("Sat Max", "Trackbar", 255, 255, empty)
cv2.createTrackbar("Val Min", "Trackbar", 156, 255, empty)  # wykonanie suwaka jasności w oknie; 0-255 poziomy
cv2.createTrackbar("Val Max", "Trackbar", 255, 255, empty)

# while True:
img = cv2.imread("Resources/tukan.jpg")
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # przełącznie przestrzeni barw z RGB na HSV
h_min = cv2.getTrackbarPos("Hue Min", "Trackbar")
h_max = cv2.getTrackbarPos("Hue Max", "Trackbar")
s_min = cv2.getTrackbarPos("Sat Min", "Trackbar")
s_max = cv2.getTrackbarPos("Sat Max", "Trackbar")
v_min = cv2.getTrackbarPos("Val Min", "Trackbar")
v_max = cv2.getTrackbarPos("Val Max", "Trackbar")
print(h_min, h_max, s_min, s_max, v_min, v_max)
lower = np.array([h_min, s_min, v_min])
upper = np.array([h_max, s_max, v_max])
mask = cv2.inRange(imgHSV, lower, upper)
imgResult = cv2.bitwise_and(img, img, mask=mask)

    # cv2.imshow("image", img)
    # cv2.imshow("imageHSV", imgHSV)
    # cv2.imshow("Mask", mask)
    # cv2.imshow("imgResoult", imgResult)

imgStack = stackImages(1, ([img, imgHSV],[mask, imgResult]))
cv2.imshow("stacked", imgStack)

cv2.waitKey(0)