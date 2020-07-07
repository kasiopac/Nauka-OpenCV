'''
wstawianie linii, prostokątow, okręgów, napisow do obrazu
'''

import cv2
import numpy as np

# punkt (0,0) jest w lewym gornym rogu obrazu

img = np.zeros((512, 512, 3), np.uint8)  # 512x512 pikseli, 3 kanały, 8 bitów: 0-255; wypełniony zerami wiec obraz jest czarny
# print(img)

imgBlue = np.copy(img) # form copy import deepcopy; deepcopy(x) - kopia wykonana przez pythona (bez numpy)
imgBlue[100:200,0:200] = 255, 0, 0  # wycinek obrazka bedzie niebieski; B=255, G=0, R=0

# cv2.imshow("Image", img)
# cv2.imshow("ImageBlue", imgBlue)

# cv2.waitKey(0)

#LINIE:
# cv2.line(img, (0, 0), (300, 300), (0, 255, 0), 3)  # linia - (obiekt, punkt statrowy, punkt koncowy, (B,G,R), grubosc)
# cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), 2)  # prostokąt- (obiekt, punkt statrowy, punkt koncowy, (B,G,R), grubosc)
# cv2.line(imgBlue, (0, 0), (imgBlue.shape[1], imgBlue.shape[0]), (0, 255, 0), 3)  # punkt koncowy szer img.shape[1], wys img.shape[0]
# cv2.rectangle(imgBlue, (0, 0), (250, 350), (0, 0, 255), cv2.FILLED)  # cv2.FILLED - wypelnienie prostokata
# cv2.circle(imgBlue, (400, 50), 30, (255,255,0), 4)  # okrąg - (obiekt, srodek, promien, kolor, grubosc linii
# cv2.putText(img, "opencv", (300,100), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 150, 0), 2)  # tekst - (obiekt, tresc, punkt startowy, czcionka, rozmiar, kolor, grubosc)

cv2.imshow("Image", img)
cv2.imshow("ImageBlue", imgBlue)
cv2.waitKey(0)