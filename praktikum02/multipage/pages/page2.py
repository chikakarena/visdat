import streamlit as st
import pandas as pd
import numpy as np

# Pastikan file ini memiliki judul dan konten visualisasi
st.title("📊 Halaman 2: Line Chart")
st.markdown("Visualisasi data acak menggunakan `st.line_chart()`.")
# Identitas Kelompok
st.write("Kelompok: 04")
st.markdown("""
- Chika Karena - 0110222015
- Chery Renata - 0110222001
- Ira Pratiwi - 0110222162
""")
# 1. Buat Data
df = pd.DataFrame(
    np.random.randn(30, 4),
    columns=['C1', 'C2', 'C3', 'C4']
)

# 2. Tampilkan Konten
st.line_chart(df)