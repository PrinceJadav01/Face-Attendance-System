import os
import csv
from datetime import datetime

def create_dataset_folder(name, student_id):
    folder_name = f"{name}_{student_id}"
    path = os.path.join("dataset", folder_name)
    os.makedirs(path, exist_ok=True)
    return path

def get_images_and_labels(dataset_path):
    import cv2
    import numpy as np

    face_samples = []
    ids = []
    label_map = {}
    current_id = 0

    for folder in os.listdir(dataset_path):
        label_map[current_id] = folder
        folder_path = os.path.join(dataset_path, folder)

        for image_name in os.listdir(folder_path):
            img_path = os.path.join(folder_path, image_name)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

            if img is None:
                continue

            face_samples.append(img)
            ids.append(current_id)

        current_id += 1

    return face_samples, ids, label_map

def mark_attendance(name, student_id):
    file_exists = os.path.isfile("attendance.csv")

    with open("attendance.csv", "a", newline="") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["Name", "ID", "Date", "Time"])

        now = datetime.now()
        date = now.strftime("%Y-%m-%d")
        time = now.strftime("%H:%M:%S")

        writer.writerow([name, student_id, date, time])