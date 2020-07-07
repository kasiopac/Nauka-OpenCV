"""
detekcja tablic rejestracyjnych i wyswietlanie bez perspektywy
"""

import cv2

#############################################
frameWidth = 640
frameHeight = 480
nPlateCascade = cv2.CascadeClassifier("Resources/haarcascade_russian_plate_number.xml")  # klasyfikator
minArea = 200
color = (255, 0, 255)
#############################################

cap = cv2.VideoCapture(0)  #
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)
count = 0

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberPlates = nPlateCascade.detectMultiScale(imgGray, 1.1, 10)  # detekcja tablic rejestracyjnych na podst. klasyfikatora
    for (x, y, w, h) in numberPlates:
        area = w * h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)  # oznaczenie ramką wykrytych tablic
            cv2.putText(img, "Number Plate", (x, y - 5),     # oznaczenie nagłowków wykrytych tablic
                        cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
            imgRoi = img[y:y + h, x:x + w] # wyznaczenie obszaru z wycinków od y do y+h i od x do x+w
            cv2.imshow("ROI", imgRoi)  # wyswietlenie samej tablicy w oddzielnym oknie

    cv2.imshow("Result", img) # wyswietlenie calego obrazu z zaznaczona tablica i ramka

    if cv2.waitKey(1) & 0xFF == ord('s'):  # po nacisnieciu klawusza s
        cv2.imwrite("Resources/Scanned/NoPlate_" + str(count) + ".jpg", imgRoi)  # zapis obrazu z tablicą
        cv2.rectangle(img, (0, 200), (640, 300), (0, 0, 0), cv2.FILLED)   # wyswietlenie prostokąta
        cv2.putText(img, "Scan Saved", (150, 265), cv2.FONT_HERSHEY_DUPLEX,  # wyswietlenie napisu o zapisie obrazu
                    2, (255, 255, 255), 2)
        cv2.imshow("Result", img)  # powrot do wyswietlania obrazu
        cv2.waitKey(500)
        count += 1
        # continue
    if cv2.waitKey(1) & 0xFF == ord('q'):  # zamykanie filmu przyciskiem q z klawiatury
        break