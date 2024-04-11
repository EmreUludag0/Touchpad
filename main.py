import cv2
import mediapipe as mp

video = cv2.VideoCapture(0)

yukseklik_esik = 50

mp_cizim = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

with mp_hands.Hands(static_image_mode=False) as  hands:
    while True:
        kontrol, kamera = video.read()

        sonuc = hands.process(cv2.cvtColor(kamera, cv2.COLOR_BGR2RGB))

        if sonuc.multi_hand_landmarks:
            for hand_landmarks in sonuc.multi_hand_landmarks:
                yukseklikler = []
                for landmark in hand_landmarks:
                    yukseklikler.append(landmark.z)
                
            parmakSayisi = 0
            for yukseklik in yukseklikler:
                if yukseklik > yukseklik_esik:
                    parmakSayisi += 1

            print("parmak sayisi", parmakSayisi)

            mp_cizim.draw_landmarks(kamera, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        cv2.imshow('El Cizimi',kamera)        

        if cv2.waitKey(10) == 27:
            break

video.release()
cv2.destroyAllWindows()
