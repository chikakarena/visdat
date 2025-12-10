import streamlit as st
import pandas as pd 
import numpy as np 

st.title("colum")
st.write("Kelompok: 34")
st.markdown("""  
- Chika Karena - 0110222015  
- Chery Renata - 0110222011  
- Ira Pratiwi - 01102222162""")
# Membuat dua kolom dengan lebar yang sama
col1, col2 = st.columns(2)
# Mengisi Kolom Pertama (col1)
col1.write("ini baris pertama")
col1.image("../assets/bunga.jpg")
# Mengisi Kolom Kedua (col2)
col2.write("ini baris")
col2.image("../assets/bunga.jpg")