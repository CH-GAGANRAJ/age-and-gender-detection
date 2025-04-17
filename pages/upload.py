import streamlit as st
import cv2
from deepface import DeepFace
from PIL import Image
import numpy as np
import os

# Function to detect age and gender
def detect_age_gender1(image_path):
    try:
        analysis = DeepFace.analyze(img_path=image_path, actions=['age', 'gender'])
        age = analysis[0]['age']
        gender = analysis[0]['dominant_gender']
        return age, gender
    except Exception as e:
        st.error(f"Error analyzing image: {e}")
        return None, None

def run1():
    st.title("Age and Gender Detection App")
    st.write("Upload an image to detect age and gender")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])


    if uploaded_file is not None:
        try:
            # Convert the uploaded file to an OpenCV image
            file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
            image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # Display the uploaded image
            st.image(image_rgb, caption='Uploaded Image.', width=500)
            st.write("")
            st.write("Detecting age and gender...")

            # Save the image temporarily to pass it to DeepFace
            temp_image_path = "temp_image.jpg"
            cv2.imwrite(temp_image_path, image)

            # Detect age and gender
            age, gender = detect_age_gender1(temp_image_path)

            if age is not None and gender is not None:
                st.info(f"Predicted Age: {age}")
                st.info(f"Predicted Gender: {gender}")

            else:
                st.write("Age and gender detection failed.")
        except Exception as e:
            st.error(f"Error processing image: {e}")
        finally:
            if os.path.exists(temp_image_path):
                os.remove(temp_image_path)

if __name__ == "__main__":
    run1()
