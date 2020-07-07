'''
Kadrowanie i ustawianie perspektywy
'''

import cv2
import numpy as np

img = cv2.imread("Resources/karty.jpg")
print(img.shape)
# cv2.line(img, (100, 72), (185, 58), (0, 255, 0), 1)
# cv2.line(img, (120, 202), (205, 190), (0, 255, 0), 1)

width, height = 200, 250
points1 = np.float32([[100,72], [185,58], [120, 202], [205,190]])
points2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(points1, points2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))


cv2.imshow("image", img)
cv2.imshow("output", imgOutput)

cv2.waitKey(0)