import streamlit as st
from PIL import Image, ImageFilter
import numpy as np

# Fungsi untuk denoising menggunakan filter median
def denoise_image_pillow(image):
    """
    Applies Median Filter for Denoising using Pillow.
    
    Args:
        image: Input image (PIL format).
        
    Returns:
        Denoised image (PIL format).
    """
    return image.filter(ImageFilter.MedianFilter(size=3))

# Halaman utama yang menampilkan anggota kelompok
def main_page():
    st.title("Linear Algebra Group 2 Class 2 [2023]")

    col1, col2 = st.columns(2)

    with col1:
        # Meminta pengguna mengunggah gambar logo jika dijalankan di cloud
        uploaded_logo = st.file_uploader("Upload University Logo", type=["png", "jpg", "jpeg"])
        if uploaded_logo is not None:
            st.image(uploaded_logo, caption="University Logo", use_column_width=True)
        else:
            st.write("Please upload the university logo.")

    with col2:
        st.write("**Group Members:**")
        st.write("- Achmad Ridho Raziqin Ahsit")
        st.write("- Dhimas Ariyanto")
        st.write("- Muhammad Isfan Nabil Hanif")
        st.write("- Pambudi Setyo Wicaksono")

# Halaman untuk denoising gambar
def denoising_page():
    st.title("Image Denoising with Pillow")

    # Meminta pengguna untuk mengunggah file gambar
    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)

        # Terapkan filter median untuk menghilangkan noise
        denoised_image = denoise_image_pillow(image)

        # Tampilkan gambar asli dan yang sudah di-denoise
        st.image([image, denoised_image], caption=['Original Image', 'Denoised Image'], use_container_width=True)

# Halaman tentang image denoising
def about_page():
    st.title("About Image Transformation: Denoiser")

    col1, col2 = st.columns(2)

    with col1:
        # Meminta pengguna mengunggah gambar denoiser effect jika dijalankan di cloud
        uploaded_image = st.file_uploader("Upload Denoiser Effect Image", type=["png", "jpg", "jpeg"], key="denoiser")
        if uploaded_image is not None:
            st.image(uploaded_image, caption="Denoiser Effect", use_column_width=True)
        else:
            st.write("Please upload the denoiser effect image.")

    with col2:
        st.write("**Image Denoising**")
        st.write("Image denoising is a technique used to reduce noise in images. Noise can be caused by various factors, such as sensor noise, transmission errors, or poor lighting conditions.")
        st.write("The **Median Filter** technique is one of the basic methods for image denoising. It works by applying a filter that preserves edges while reducing noise, making it suitable for basic denoising operations.")

# Menentukan halaman berdasarkan pilihan di sidebar
if __name__ == "__main__":
    page = st.sidebar.selectbox("Select a Page", ["1. Linear Algebra Project", "2. Image Transformation: Denoiser", "3. About Image Transformation"])

    if page == "1. Linear Algebra Project":
        main_page()
    elif page == "2. Image Transformation: Denoiser":
        denoising_page()
    elif page == "3. About Image Transformation":
        about_page()
