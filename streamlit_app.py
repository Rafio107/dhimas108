import streamlit as st
from PIL import Image, ImageFilter

def denoise_image_pillow(image):
    """
    Applies Median Filter for Denoising using Pillow.
    
    Args:
        image: Input image (PIL format).
        
    Returns:
        Denoised image (PIL format).
    """
    return image.filter(ImageFilter.MedianFilter(size=3))

def main_page():
    st.title("Linear Algebra Group 2 Class 2 [2023]")

    col1, col2 = st.columns(2)

    with col1:
        # Gunakan URL atau pastikan path lokal bisa diakses
        st.image("https://your-image-url.com/PresidentUniversityLogo.png")

    with col2:
        st.write("**Group Members:**")
        st.write("- Achmad Ridho Raziqin Ahsit")
        st.write("- Dhimas Ariyanto")
        st.write("- Muhammad Isfan Nabil Hanif")
        st.write("- Pambudi Setyo Wicaksono")

def denoising_page():
    st.title("Image Denoising with Pillow")

    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)

        # Apply denoising using Pillow's Median Filter
        denoised_image = denoise_image_pillow(image)

        # Display both original and denoised images
        st.image([image, denoised_image], caption=['Original Image', 'Denoised Image'], use_container_width=True)

def about_page():
    st.title("About Image Transformation: Denoiser")

    col1, col2 = st.columns(2)

    with col1:
        # Gunakan URL atau pastikan path lokal bisa diakses
        st.image("https://your-image-url.com/DenoiserEffect.png")

    with col2:
        st.write("**Image Denoising**")
        st.write("Image denoising is a technique used to reduce noise in images. Noise can be caused by various factors, such as sensor noise, transmission errors, or poor lighting conditions.")
        st.write("The **Median Filter** technique is one of the basic methods for image denoising. It works by applying a filter that preserves edges while reducing noise, making it suitable for basic denoising operations.")

if __name__ == "__main__":
    page = st.sidebar.selectbox("Select a Page", ["1. Linear Algebra Project", "2. Image Transformation: Denoiser", "3. About Image Transformation"])

    if page == "1. Linear Algebra Project":
        main_page()
    elif page == "2. Image Transformation: Denoiser":
        denoising_page()
    elif page == "3. About Image Transformation":
        about_page()
