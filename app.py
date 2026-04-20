import streamlit as st
import cv2

st.title("Face Attendance System")

run = st.button("Start Camera")

if run:
    cap = cv2.VideoCapture(0)
    stframe = st.empty()

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        stframe.image(frame, channels="BGR")