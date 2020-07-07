'''
Wyswietlanie obrazu i wideo w opencv
'''

import cv2

# img = cv2.imread("Resources/piesel.jpg") # wczytanie obrazu
#
# cv2.imshow("Output", img)  # wyświetlenie; obraz pojawia się na moment i znika
# cv2.waitKey(0)    # program czeka na nacisniecie przycisku przez: 1 - 1 milisekunda; 1000 - i sekunda itd;  0 - zatrzymanie obrazu do czasu wcisniecia jakiegos przycisku


# cap = cv2.VideoCapture("Resources/jezioro.mp4")
cap = cv2.VideoCapture(0)  # 0 - defoultowa kamera laptopa; inna cyfra to ID kamery
cap.set(3, 640)  # 3 - szerokość obrazu
cap.set(4, 480)  # 4 - wysokość obrazu
cap.set(10,10)  # 10 - ustawienie jasności; nie wiem czemu u mnie nic nie zmieniają


while True:
    success, vid = cap.read()  # success - wartosc True/False
    cv2.imshow("video", vid)   # wyswietlenie obrazu
    if cv2.waitKey(1) & 0xFF == ord('q'):  # zamykanie filmu przyciskiem q z klawiatury
        break