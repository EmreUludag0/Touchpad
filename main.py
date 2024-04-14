import cv2
import mediapipe as mp
import time
import ctypes

video = cv2.VideoCapture(0)


mp_cizim = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

yukseklik_esik = 0.5 #0.5'ten buyukse parmak olarak kabul edilir


with mp_hands.Hands(static_image_mode=False) as  hands:
    while True:
        kontrol, kamera = video.read()

        rgb = cv2.cvtColor(kamera, cv2.COLOR_BGR2RGB)
        sonuc = hands.process(rgb)
        yedekParmakSayisi = None

        # parmak index atama kısmı
        if sonuc.multi_hand_landmarks:
            for hand_landmarks in sonuc.multi_hand_landmarks:
                yukseklikler = [landmark.y for landmark in hand_landmarks.landmark] #normalleştirilmiş yukseklik listesi                
                
                parmakSayisi = sum(y > yukseklik_esik for y in yukseklikler)
                
                print("parmak sayisi", parmakSayisi)                

                mp_cizim.draw_landmarks(kamera, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                
            yedekParmakSayisi = parmakSayisi

        komut1 = 18
        komut2 = 15
        komut3 = 12
        komut4 = 10
        komut5 = 9

        
        time.sleep(2)
        if(yedekParmakSayisi == komut1):
            ctypes.windll.user32.LockWorkStation()
            break
        elif(yedekParmakSayisi == komut2):
            
            break
        elif(yedekParmakSayisi == komut3):
            print("3 parmak gösteriliyor")
            break
        elif(yedekParmakSayisi == komut4):
            print("4 parmak gösteriliyor")
            break
        elif(yedekParmakSayisi == komut5):
            print("5 parmak gösteriliyor")
            break



        cv2.imshow('El Cizimi',kamera)        

        if cv2.waitKey(10) == 27:
            break

video.release()
cv2.destroyAllWindows()
