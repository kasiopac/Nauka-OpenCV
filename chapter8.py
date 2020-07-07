'''
detekcja ksztaltów
'''

import cv2
import numpy as np
from stack import stackImages  # funkcja do ustawiania obrazow obok siebie i pod sobą

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # znajduje kontury w obrazie img, cv2.RETR_EXTERNAL - kontury ZEWNETRZNE, cv2.CHAIN_APPROX_NONE - bez aproksymacji, czyli wykorzystujemy wszystkie kontury
    for cnt in contours:
        area = cv2.contourArea(cnt)  # znalezienie obszaru zakreslonego konturami
        print(area)
        if area > 500:  # dla obszarow wiekszych niz 500 pikseli
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)  # pogrubienie znalezionych konturów
            peri = cv2.arcLength(cnt, True)  # wyznaczenie dlugosci krawedzi
            # print(peri)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)  # znalezienie narozników; True - znaczy ze szukamy krawędzi ktore sa zamknięte, nie otwarte
            print(len(approx))
            objCor = len(approx)  # wyznaczenie ilosci wierzchołków (sa zwracane w liscie, wiec wyznaczamy ilosc elementow listy)
            x, y, w, h = cv2.boundingRect(approx)  # wyznaczenie wpolrzednych wierzcholkow i odleglosci miedzy nimi
            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 2)  # nalozenie ramki na znalezione wierzcholki

            if objCor == 3:
                ObjectType = "Tri"
            elif objCor == 4:
                aspRatio = w / float(h)
                if aspRatio > 0.95 and aspRatio < 1.05:
                    ObjectType = "Square"
                else: ObjectType = "Rectangle"
            elif objCor > 4: ObjectType = "Circle"
            else: ObjectType = "None"

            cv2.putText(imgContour, ObjectType, (x + (w // 2) - 10, y + (h // 2)-10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 2)


kernel = np.ones((2, 2), np.uint8)  # potrzebne do pogrubienia krawedzi w funkcji cv2.dilate
img = cv2.imread("Resources/figury.jpg")
imgContour = img.copy()  # kopia img wykorzystana w funkcji getContours (powyzej)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)   # znalezienie krawedzi obrazu
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)  # pogrubienie krawędzi
getContours(imgDialation)

imgStack = stackImages(0.5, ([img, imgBlur, imgGray], ([imgCanny, imgDialation, imgContour])))

cv2.imshow("stack", imgStack)

cv2.waitKey(0)