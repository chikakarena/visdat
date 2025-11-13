import streamlit as st

st.title("Column")
st.write("Kelompok: 34")
st.markdown("""  
- Chika Karena - 0110222015  
- Chery Renata - 0110222011  
- Ira Pratiwi - 01102222162""")

col1, col2 += st.columns(2)             

col1.write("ini adalah kolom pertama")
col1.image()
col2.write("ini adalah kolom kedua")
col2.write
