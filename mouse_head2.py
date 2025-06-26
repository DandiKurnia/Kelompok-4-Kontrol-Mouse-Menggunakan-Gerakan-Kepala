import cv2
import numpy as np
import pyautogui
import time

# Inisialisasi kamera
cap = cv2.VideoCapture(0)

# Load Haar Cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")

# Ukuran layar
screen_width, screen_height = pyautogui.size()

# Smoothing
smooth_x, smooth_y = 0, 0
alpha = 0.2

# Waktu jeda klik
click_cooldown = 1.5
last_click_time = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces[:1]:
        face_center_x = x + w // 2
        face_center_y = y + h // 2

        cam_height, cam_width = frame.shape[:2]
        screen_x = int(screen_width * face_center_x / cam_width)
        screen_y = int(screen_height * face_center_y / cam_height)

        smooth_x = int(smooth_x + alpha * (screen_x - smooth_x))
        smooth_y = int(smooth_y + alpha * (screen_y - smooth_y))

        pyautogui.moveTo(smooth_x, smooth_y)

        # Gambar kotak wajah
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.circle(frame, (face_center_x, face_center_y), 5, (255, 0, 0), -1)

        # ROI senyum
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        smiles = smile_cascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.7,
            minNeighbors=22,
            minSize=(25, 25)
        )

        # Deteksi senyum (gigi terlihat)
        if len(smiles) > 0:
            now = time.time()
            if now - last_click_time > click_cooldown:
                pyautogui.click()
                print("Click by smile!")
                last_click_time = now

        # Gambar kotak senyum
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (255, 0, 255), 2)

    cv2.imshow("Head Mouse Control + Smile Click", frame)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
