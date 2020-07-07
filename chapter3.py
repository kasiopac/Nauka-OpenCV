'''
resize, wycinki obrazu
'''

import cv2
import numpy as np

# w poleceniach cv2 podajemy najpierw szerokosc, potem wysokosc; w poleceniach pythona najpierw wysokosc potem szerokossc
img = cv2.imread("Resources/tukan.jpg")
print(img.shape)  # zwraca: wysokosc, szerokosc, il. kanałow(3= RGB)

imgResize = cv2.resize(img, (400,100)) # nowe wymiary
# print(imgResize.shape)

imgCropped = img[0:100, 100:200]  #  wycinek obrazu: [wysokosc, szerokosc] !!

cv2.imshow("Tukan", img)
cv2.imshow("TukanResized", imgResize)
cv2.imshow("TukanCropped", imgCropped)
cv2.waitKey(0)