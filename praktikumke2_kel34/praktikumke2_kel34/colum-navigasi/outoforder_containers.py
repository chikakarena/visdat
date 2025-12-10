import streamlit as st
import pandas as pd 
import numpy as np 

st.title("Out of Order Container")
st.write("Kelompok: 34")
st.markdown("""  
- Chika Karena - 0110222015  
- Chery Renata - 0110222011  
- Ira Pratiwi - 01102222162""")

st.title("Out of Order Container")

# Defining Containers
container_one = st.container()
container_one.write("Element One Inside Container")
st.write("Element Outside Container")

# Now insert few more elements in the container_one
container_one.write("Element Two Inside Container")
container_one.line_chart(np.random.randn(40, 4))