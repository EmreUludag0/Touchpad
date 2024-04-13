import cv2
import mediapipe as mp
import os 

video = cv2.VideoCapture(0)


mp_cizim = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

yukseklik_esik = 0.5 #0.5'ten buyukse parmak olarak kabul edilir


with mp_hands.Hands(static_image_mode=False) as  hands:
    while True:
        kontrol, kamera = video.read()

        rgb = cv2.cvtColor(kamera, cv2.COLOR_BGR2RGB)
        sonuc = hands.process(rgb)

        # parmak index atama kısmı
        if sonuc.multi_hand_landmarks:
            for hand_landmarks in sonuc.multi_hand_landmarks:
                yukseklikler = [landmark.y for landmark in hand_landmarks.landmark] #normalleştirilmiş yukseklik listesi                
                
                parmakSayisi = sum(y > yukseklik_esik for y in yukseklikler)
                
                print("parmak sayisi", parmakSayisi)                

                mp_cizim.draw_landmarks(kamera, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                if (parmakSayisi == 18) or (parmakSayisi == 19):
                    print("1 parmak gösteriliyor")
                    break
                elif (parmakSayisi == 17) or (parmakSayisi == 16):
                    print("2 parmak gösteriliyor")
                    break
                elif (parmakSayisi == 14) or (parmakSayisi == 13) or (parmakSayisi == 12):
                    print("3 parmak gösteriliyor")
                    break
                elif (parmakSayisi == 11) or (parmakSayisi == 10):
                    print("4 parmak gösteriliyor")
                    break
                elif (parmakSayisi == 9):
                    print("5 parmak gösteriliyor")
                    break


        cv2.imshow('El Cizimi',kamera)        

        if cv2.waitKey(10) == 27:
            break

video.release()
cv2.destroyAllWindows()
