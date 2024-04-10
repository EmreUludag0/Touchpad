import cv2
import mediapipe as mp

video = cv2.VideoCapture(0)

mp_cizim = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

with mp_hands.Hands(static_image_mode=False) as  hands:
    while True:
        kontrol, kamera = video.read()

        sonuc = hands.process(cv2.cvtColor(kamera, cv2.COLOR_BGR2RGB))

        if sonuc.multi_hand_landmarks != None:
            for handLandmarks in sonuc.multi_hand_landmarks:
                mp_cizim.draw_landmarks(kamera,handLandmarks, mp_hands.HAND_CONNECTIONS)
        cv2.imshow('deneme',kamera)        

        if cv2.waitKey(10) == 27:
            break


