import streamlit as st
import pandas as pd 
import numpy as np 

st.title("Container")
st.write("Kelompok: 34")
st.markdown("""  
- Chika Karena - 0110222015  
- Chery Renata - 0110222011  
- Ira Pratiwi - 01102222162""")

st.title("Container")
with st.container():
    st.write("Element Inside Contianer")
    # Defining Chart Element
    st.line_chart(np.random.randn(40, 4))
st.write("Element Outside Container")