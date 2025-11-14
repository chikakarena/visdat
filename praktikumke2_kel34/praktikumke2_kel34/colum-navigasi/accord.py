import streamlit as st
import pandas as pd 
import numpy as np 

st.title("Exapanders/Accordions")
st.write("Kelompok: 34")
st.markdown("""  
- Chika Karena - 0110222015  
- Chery Renata - 0110222011  
- Ira Pratiwi - 01102222162""")

st.title('Exapanders/Accordions')

# Mendefinisikan Expander
with st.expander("Streamlit with Python"):
    st.write("Kembangkan Aplikasi ML dalam Hitungan Menit!!!")