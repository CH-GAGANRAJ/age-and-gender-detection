import age as ag
import streamlit as st

st.title('AGE AND GENDER DETECTION MODEL')
st.info('Welcome to the Real-Time Dominant Gender Detection project! '
        'This innovative application leverages advanced facial recognition technology to '
        'identify and display the dominant gender in real-time using live video feeds from'
        ' your webcam. By combining the power of the DeepFace library with the user-friendly '
        'Streamlit interface, we aim to deliver'
        ' a seamless and efficient gender detection solution suitable '
        'for various applications.')
a=st.button('Live web cam')
st.info('The above button will open your real time webcam')
b=st.button('upload image')
st.info('The above button will help you to upload images.')
if a:
    ag.run()
if b:
    st.info("Go To upload page.....")
