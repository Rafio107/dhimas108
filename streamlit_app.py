import streamlit as st
from PIL import Image
import io

# Fungsi untuk memeriksa format file yang diperbolehkan
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Fungsi untuk mengompres gambar
def compress_image(image, quality=50):
    img = Image.open(image)
    
    # Convert image to JPEG format if it is not already JPEG
    if img.mode in ("RGBA", "P"):  # Convert png with transparency to RGB
        img = img.convert("RGB")
    
    compressed_image = io.BytesIO()  # Buffer untuk gambar terkompresi
    img.save(compressed_image, format="JPEG", optimize=True, quality=quality)
    compressed_image.seek(0)  # Kembali ke posisi awal setelah menulis
    return compressed_image

# CSS untuk tampilan custom di Streamlit
def custom_css():
    st.markdown("""
    <style>
    body {
        font-family: 'Courier New', Courier, monospace;
        background-color: #ADD8E6; /* Ubah latar belakang ke biru muda */
        color: #000000; /* Warna teks hitam */
        margin: 0;
        text-align: center;
        padding: 50px;
    }
    </style>
    """, unsafe_allow_html=True)

# Main Streamlit App
def main():
    st.title("Pixel Compress")
    st.write("Compress your photos in a pixelated style!")

    # Mengupload gambar
    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg", "gif"])

    if uploaded_file is not None:
        if allowed_file(uploaded_file.name):  # Periksa format file
            # Tampilkan gambar yang diupload
            st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

            # Kompres gambar
            if st.button("Compress Image"):
                with st.spinner("Compressing..."):
                    try:
                        compressed_img = compress_image(uploaded_file)

                        # Tampilkan gambar hasil kompresi
                        st.image(compressed_img, caption="Compressed Image", use_column_width=True)

                        # Tombol untuk mendownload gambar terkompresi
                        st.download_button(
                            label="Download Compressed Image",
                            data=compressed_img,
                            file_name="compressed_image.jpg",
                            mime="image/jpeg"
                        )
                    except Exception as e:
                        st.error(f"An error occurred: {e}")
        else:
            st.error("The uploaded file format is not supported. Please upload a valid image.")
    else:
        st.info("Please upload an image file.")

if __name__ == "__main__":
    custom_css()
    main()
