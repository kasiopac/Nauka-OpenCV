'''
"rysowanie śladów" przedmiotami w kolorze pomaranczowym, fioletowym i zielonym
'''


import cv2
import numpy as np

cap = cv2.VideoCapture(0)  # 0 - defoultowa kamera laptopa; inna cyfra to ID kamery
cap.set(3, 640)  # 3 - szerokość obrazu
cap.set(4, 480)  # 4 - wysokość obrazu
cap.set(10,150)  # 10 - ustawienie jasności; nie wiem czemu u mnie nic nie zmieniają

myColors = [[5, 107, 0, 19, 255, 255] ,   # podanie zakresów kolorow które mają byc wykryte
            [133, 56, 0, 159, 156, 255],
            [57, 76, 0, 100, 255, 255]]

myColorValues = [[51, 153, 255],   # podanie kolorow które m
                 [255, 0, 255],
                 [0, 255, 0]]

myPoints = []  ## [x , y , colorId ]

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # znajduje kontury w obrazie img, cv2.RETR_EXTERNAL - kontury ZEWNETRZNE, cv2.CHAIN_APPROX_NONE - bez aproksymacji, czyli wykorzystujemy wszystkie kontury
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)  # znalezienie obszaru zakreslonego konturami
        if area > 500:  # dla obszarow wiekszych niz 500 pikseli
            # cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)  # pogrubienie znalezionych konturów
            peri = cv2.arcLength(cnt, True)  # wyznaczenie dlugosci krawedzi
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)  # znalezienie narozników; True - znaczy ze szukamy krawędzi ktore sa zamknięte, nie otwarte
            x, y, w, h = cv2.boundingRect(approx)  # wyznaczenie wpolrzednych wierzcholkow i odleglosci miedzy nimi
    return  x+w//2, y    # zwraca wspolrzedne punktu na srodku gornej krawedzi bounding boxa


def findColor(img, myColors, myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # zmiana na przestrzen kolorow hsv
    count = 0  # licznik kolorow
    newPoints = []
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)  # nalozenie maski wyodrebniajacej odpowiedni kolor
        x, y = getContours(mask)    # pobranie wspolrzednych punktu na srodku gornej krawedzi bounding boxa
        cv2.circle(imgResult, (x, y), 15, myColorValues[count], cv2.FILLED)  # wyswietlenie punktu w postaci małego kołą
        if x != 0 and y != 0:
            newPoints.append([x, y, count])  # dodanie kolejnych punktow do listy
        count += 1
        # cv2.imshow(str(color[0]),mask)
    return newPoints


def drawOnCanvas(myPoints, myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)  # wyswietlenie pozostalych punktow w postaci kółek


while True:
    success, img = cap.read()  # success - wartosc True/False
    imgResult = img.copy()
    newPoints = findColor(img, myColors, myColorValues)
    if len(newPoints) != 0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints)  != 0:
        drawOnCanvas(myPoints, myColorValues)

    cv2.imshow("video", imgResult)  # wyswietlenie obrazu

    if cv2.waitKey(1) & 0xFF == ord('q'):  # zamykanie filmu przyciskiem q z klawiatury
        break
