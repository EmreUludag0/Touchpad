import cv2
import mediapipe as mp

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

        cv2.imshow('El Cizimi',kamera)        

        if cv2.waitKey(10) == 27:
            break

video.release()
cv2.destroyAllWindows()
