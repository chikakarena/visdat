import streamlit as st
import graphviz as graphviz

st.title("graphviz_chart")
st.write("Kelompok: 34")
st.markdown("""  
- Chika Karena - 0110222015  
- Chery Renata - 0110222011  
- Ira Pratiwi - 01102222162""")

import streamlit as st
import graphviz as graphviz

st.title('Graphviz')

# Membuat grafik menggunakan teks Graphviz langsung
st.graphviz_chart('''
digraph {
    "Training Data" -> "ML Algorithm"
    "ML Algorithm" -> "Model"
    "Model" -> "Result Forecasting"
    "New Data" -> "Model"
}
''')