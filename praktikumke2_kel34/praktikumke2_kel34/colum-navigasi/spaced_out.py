import streamlit as st
import pandas as pd 
import numpy as np 

st.title("spaced out ")
st.write("Kelompok: 34")
st.markdown("""  
- Chika Karena - 0110222015  
- Chery Renata - 0110222011  
- Ira Pratiwi - 01102222162""")

from PIL import Image
img = Image.open("../assets/bunga.jpg")
st.title("Spaced-Out Columns")

# Mendefinisikan dua Baris 
for _ in range(2):
# Mendefinisikan jumlah kolom dengan ukuran 
    cols = st.columns((3, 1, 2, 1))
    cols[0].image(img)
    cols[1].image(img)
    cols[2].image(img)
    cols[3].image(img)