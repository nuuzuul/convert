import streamlit as st
from pdf2docx import Converter
from io import BytesIO
import os

def pdf_to_word(pdf_file):
    # Menyimpan file PDF
    with open("temp.pdf", "wb") as f:
        f.write(pdf_file.getbuffer())
    
    # Membuat objek konversi PDF ke Word
    cv = Converter("temp.pdf")
    
    # Simpan ke file Word
    word_file = BytesIO()
    cv.convert(word_file) 
    word_file.seek(0)
    
    # Tutup konverter
    cv.close()
    
    return word_file

# Judul aplikasi
st.title("Konversi PDF ke Word")

# Mengunggah file PDF
uploaded_file = st.file_uploader("Unggah file PDF", type="pdf")

# Jika file telah diunggah
if uploaded_file:
    # Mengambil nama file PDF yang diunggah
    pdf_filename = uploaded_file.name
    word_filename = os.path.splitext(pdf_filename)[0] + ".docx"
    
    # Tombol untuk melakukan konversi
    if st.button("Konversi ke Word"):
        word_file = pdf_to_word(uploaded_file)
        
        # Tautan unduh untuk file Word yang dihasilkan dengan nama yang sesuai
        st.download_button(
            label="Unduh file Word",
            data=word_file,
            file_name=word_filename,
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
