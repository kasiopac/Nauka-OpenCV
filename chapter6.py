'''
Multiplikowanie obrazu
'''

import cv2
import numpy as np
from stack import stackImages

img = cv2.imread("Resources/piesel.jpg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# imgHor = np.hstack((img, img))  # ustawienie obrazow kolo siebie
# imgVer = np.vstack((img, img))  # ustawienei obrazow nad sobą
#
# cv2.imshow("Horizontal", imgHor)
# cv2.imshow("Vertical", imgVer)




imgStack = stackImages(0.5,([img, imgGray, img], [imgGray, img, imgGray]))
cv2.imshow("Vertical", imgStack)
cv2.waitKey(0)