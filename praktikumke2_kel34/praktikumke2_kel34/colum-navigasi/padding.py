import streamlit as st
import pandas as pd 
import numpy as np 

st.title("padding")
st.write("Kelompok: 34")
st.markdown("""  
- Chika Karena - 0110222015  
- Chery Renata - 0110222011  
- Ira Pratiwi - 01102222162""")

from PIL import Image

# Membuka gambar dan menyimpannya di variabel 'img'
img = Image.open("../assets/bunga.jpg")

# Menampilkan judul di aplikasi Streamlit
st.title("Padding")

# Mendefinisikan Jarak (Padding) dengan kolom
col1, padding, col2 = st.columns((10, 2, 10))

# Mengisi Kolom 1
col1.write("ini baris pertama")
with col1:
    col1.image(img)

# Mengisi Kolom 2
col2.write("ini baris ke dua")
with col2:
    col2.image(img)
