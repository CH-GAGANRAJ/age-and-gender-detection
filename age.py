import streamlit as st
import cv2
from deepface import DeepFace
import numpy as np


# Function to detect faces using OpenCV
def detect_faces(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return faces


# Function to detect age and gender
def detect_age_gender(face):
    try:
        # Analyze the face with DeepFace
        analysis = DeepFace.analyze(face, actions=['age', 'gender'],enforce_detection=False)
        age = analysis[0]['age']
        gender = analysis[0]['dominant_gender']
        return age, gender
    except Exception as e:
        st.error(f"Error analyzing face: {str(e)}")
        return None, None

def run():
# Streamlit interface
    st.title("Real-Time Age and Gender Detection")
    st.write("Allow camera access to start the detection")

    # Access the webcam
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        st.error("Error: Could not open webcam.")

    frame_placeholder = st.empty()

    while camera.isOpened():
        ret, frame = camera.read()
        if not ret:
            st.error("Error: Failed to capture frame from webcam.")
            break

        # Detect faces
        faces = detect_faces(frame)

        # For each face, detect age and gender
        for (x, y, w, h) in faces:
            face = frame[y:y + h, x:x + w]
            face_rgb = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
            age, gender = detect_age_gender(face_rgb)

            # Draw a rectangle around the face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Display age and gender
            if age and gender:
                cv2.putText(frame, f'Age: {age}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
                cv2.putText(frame, f'Gender: {gender}', (x, y + h + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

        # Display the frame in Streamlit
        frame_placeholder.image(frame, channels="BGR")

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()
