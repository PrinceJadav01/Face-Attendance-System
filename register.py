import cv2
import os
from utils import create_dataset_folder

def register_student(name, student_id):
    path = create_dataset_folder(name, student_id)

    cam = cv2.VideoCapture(0)
    detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    count = 0

    while True:
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = detector.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            count += 1
            face = gray[y:y+h, x:x+w]

            file_name = os.path.join(path, f"{count}.jpg")
            cv2.imwrite(file_name, face)

            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)

        cv2.imshow("Register Face", img)

        if cv2.waitKey(1) == ord('q') or count >= 40:
            break

    cam.release()
    cv2.destroyAllWindows()