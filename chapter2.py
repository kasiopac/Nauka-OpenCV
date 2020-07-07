'''
Obróbka obrazu - filtrowanie kolorow, blurowanie, znajdowanie krawedzi, wzmacnianie krawędzi'
'''

import cv2
import numpy as np


img = cv2.imread("Resources/tukan.jpg")
kernel = np.ones((2, 2), np.uint8)   # 8 bitów, czyli wartosci od 0 do 255;

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # RGB to w opencv BGR; BGR2GRAY - zamien rgb na szary
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)  # obraz wyblurowany - rozmazany
imgCanny = cv2.Canny(img, 80, 80)  # obraz zawierający tylko krawędzie
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)  # cv2.dilate pozwala pogrubic krawędzie (obraz, kernel = macierz, ktora definiuje rozmiar powiekszonych krawędzi, ilosc iteracji)
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)


# cv2.imshow("Gray Image", imgGray)
# cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)