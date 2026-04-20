import cv2
import pickle
from utils import mark_attendance

def take_attendance():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("trainer.yml")

    with open("labels.pkl", "rb") as f:
        label_map = pickle.load(f)

    cam = cv2.VideoCapture(0)
    detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    marked = set()

    while True:
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = detector.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            face = gray[y:y+h, x:x+w]
            id_, confidence = recognizer.predict(face)

            if confidence < 70:
                label = label_map[id_]
                name, student_id = label.split("_")

                if label not in marked:
                    mark_attendance(name, student_id)
                    marked.add(label)

                # text = f"{name}"   # or simply:  text = name
                text = f"{name} ({round(confidence,2)})"
            else:
                text = "Unknown"

            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            cv2.putText(img, text, (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)

        cv2.imshow("Attendance", img)

        if cv2.waitKey(1) == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()