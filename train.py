import cv2
import numpy as np
from utils import get_images_and_labels
import pickle

def train_model():
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    faces, ids, label_map = get_images_and_labels("dataset")

    # ✅ FIX: Convert ids list to numpy array
    ids = np.array(ids)

    if len(faces) == 0:
        print("No data found. Please register students first.")
        return

    recognizer.train(faces, ids)
    recognizer.save("trainer.yml")

    # Save label map
    with open("labels.pkl", "wb") as f:
        pickle.dump(label_map, f)

    print("Model trained successfully!")