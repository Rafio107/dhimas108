import streamlit as st
import cv2
import numpy as np

def denoise_nlm(img, h=10, templateWindowSize=7, searchWindowSize=21):
    """
    Applies Non-Local Means Denoising to an image.
pip freeze > requirements.txt
    Args:
        img: Input image.
        h: Parameter controlling the degree of filtering.
        templateWindowSize: Size of the template window.
        searchWindowSize: Size of the search window.

    Returns:
        Denoised image.
    """

    dst = cv2.fastNlMeansDenoisingColored(img, None, h, templateWindowSize, searchWindowSize)
    return dst

def main_page():
    st.title("Linear Algebra Group 2 Class 2 [2023]")

    col1, col2 = st.columns(2)

    with col1:
        st.image("c:\MainStorageVault\Documents\Project\ImageRestore_Project\PresidentUniversityLogo.png")

    with col2:
        st.write("**Group Members:**")
        st.write("- Achmad Ridho Raziqin Ahsit")
        st.write("- Dhimas Ariyanto")
        st.write("- Muhammad Isfan Nabil Hanif")
        st.write("- Pambudi Setyo Wicaksono")

def denoising_page():
    st.title("Image Denoising")

    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)

        denoised_img = denoise_nlm(img)

        st.image([img, denoised_img], caption=['Original Image', 'Denoised Image'])

def about_page():
    st.title("About Image Transformation: Denoiser")

    col1, col2 = st.columns(2)

    with col1:
        st.image("c:\MainStorageVault\Documents\Project\ImageRestore_Project\DenoiserEffect.png")  # Replace with your image path

    with col2:
        st.write("**Image Denoising**")
        st.write("Image denoising is a technique used to reduce noise in images. Noise can be caused by various factors, such as sensor noise, transmission errors, or poor lighting conditions.")
        st.write("The **Non-Local Means (NLM)** algorithm is a popular technique for image denoising. It works by comparing a pixel with its similar neighbors in a larger search window. It then averages the values of these similar pixels to estimate the true value of the noisy pixel.")

if __name__ == "__main__":
    page = st.sidebar.selectbox("Select a Page", ["1. Linear Algebra Project", "2. Image Transformation: Denoiser", "3. About Image Transformation"])

    if page == "1. Linear Algebra Project":
        main_page()
    elif page == "2. Image Transformation: Denoiser":
        denoising_page()
    elif page == "3. About Image Transformation":
        about_page()
