'''
detekcja dokumentow i wyswietlanie bez perspektywy
'''


import cv2
import numpy as np
from stack import stackImages


widthImg = 540
heightImg = 640
cap = cv2.VideoCapture(0)
cap.set(10, 150)


def preProcessing(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
    imgCanny = cv2.Canny(imgBlur, 200, 200)  # wyodrebnienie krawedzi na obrazie
    kernel = np.ones((5, 5))
    imgDial = cv2.dilate(imgCanny, kernel, iterations=2)  # pogrubienie krawedzi w celu polaczenia przypadkowo przerwanych krawedzi
    imgThres = cv2.erode(imgDial, kernel, iterations=1)  # pocienienie krawędzi
    return imgThres


def getContours(img):
    biggest = np.array([])
    maxArea = 0
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # znajduje kontury w obrazie img, cv2.RETR_EXTERNAL - kontury ZEWNETRZNE, cv2.CHAIN_APPROX_NONE - bez aproksymacji, czyli wykorzystujemy wszystkie kontury
    for cnt in contours:
        area = cv2.contourArea(cnt)  # znalezienie obszaru zakreslonego konturami
        if area > 5000:
            # cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)  # wyznaczenie dlugosci krawedzi
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)   # znalezienie narozników; True - znaczy ze szukamy krawędzi ktore sa zamknięte, nie otwarte
            if area > maxArea and len(approx) == 4:  # szukanie najwiekszego prostokatnego ksztaltu w obrazie
                biggest = approx
                maxArea = area
    cv2.drawContours(imgContour, biggest, -1, (255, 0, 0), 20)  # narysowanie konturu najwiekszego prostokatnego ksztaltu w obrazie
    return biggest


def reorder(myPoints):  # ustalenie kolejnosci wierzchołków wykrytego prostokąta tak by odpowiadała pts2 w funkcji getWarp
    myPoints = myPoints.reshape((4, 2))  # zmiana macierzy z 4x2x1 (czyli z [[[ , ]], [[ , ]], [[ , ]], [[ , ]]] na [[ , ], [ , ], [ , ], [ , ]] )
    myPointsNew = np.zeros((4, 1, 2), np.int32)  # utworzenie nowej macierzy dla wspolrzednych uporzadkowanych wierzcholkow
    add = myPoints.sum(1)  # sumuje wspolrzedne x i y kazdego punktu
    myPointsNew[0] = myPoints[np.argmin(add)]  # wyznaczenie punktu w lewym górnym rogu
    myPointsNew[3] = myPoints[np.argmax(add)]  # wyznaczenie punktu w prawym dolnym rogu
    diff = np.diff(myPoints, axis=1)  # diff oblicza roznice, (axis: 0=x, 1=y)
    myPointsNew[1] = myPoints[np.argmin(diff)]  # wyznaczenie punktu w prawym gornym rogu
    myPointsNew[2] = myPoints[np.argmax(diff)]  # wyznaczenie punktu w lewym dolnym rogu
    return myPointsNew


def getWarp(img, biggest):  # eliminowanie perspektywy
    biggest = reorder(biggest)  #
    pts1 = np.float32(biggest)  # puknty wierzcholkow wykrytego prostokąta
    pts2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])  # dokument ma miec wymiary okna
    matrix = cv2.getPerspectiveTransform(pts1, pts2)  # eliminowanie perspektywy
    imgOutput = cv2.warpPerspective(img, matrix, (widthImg, heightImg))

    imgCropped = imgOutput[20:imgOutput.shape[0] - 20, 20:imgOutput.shape[1] - 20]  # usunięcie 20 pixeli na obwodzie zeby usunac artefakty
    imgCropped = cv2.resize(imgCropped, (widthImg, heightImg))

    return imgCropped

while True:
    success, img = cap.read()
    img = cv2.resize(img, (widthImg, heightImg))
    imgContour = img.copy()

    imgThres = preProcessing(img)  # wyroznienie i poprawienie krawędzi
    biggest = getContours(imgThres) # znalezienie i wyznaczenie konturów najwiekszego prostokąta na obrazie
    if biggest.size != 0:
        imgWarped = getWarp(img, biggest)   # wyeliminowanie perspektywy
        imageArray = ([img,imgThres],
                  [imgContour,imgWarped])
        cv2.imshow("ImageWarped", imgWarped)
    else:
        imageArray = ([img, imgThres])  # zeby nie wywalilo bledu - przy braku prostokata na ekranie wyswietla tylko te obrazy


    stackedImages = stackImages(0.6, imageArray)
    cv2.imshow("WorkFlow", stackedImages)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # zamykanie filmu przyciskiem q z klawiatury
        break
