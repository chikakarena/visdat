import streamlit as st
import pandas as pd 
import numpy as np 
import time

st.title("Empty containers")
st.write("Kelompok: 34")
st.markdown("""  
- Chika Karena - 0110222015  
- Chery Renata - 0110222011  
- Ira Pratiwi - 01102222162""")

with st.empty():
    for second in range(5):
        st.write(f"{second} seconds have passed")
        time.sleep(1)
st.write("Times Up!")