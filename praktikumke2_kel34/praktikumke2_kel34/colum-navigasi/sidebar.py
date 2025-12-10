import streamlit as st
import pandas as pd
import numpy as np

# --- Identitas Kelompok (Bagian Utama) ---
st.title("Aplikasi dengan Sidebar Interaktif")
st.write("Kelompok: 04")
st.markdown("""
- chika Karena - 0110222015
- Chery Renata - 0110222001
- Ira Pratiwi - 0110222162
""")
st.write("Gunakan Sidebar di sebelah kiri untuk berinteraksi.")

# --- Bagian Sidebar ---
st.sidebar.title("Pengaturan Visualisasi")
st.sidebar.write("Sesuaikan parameter di sini.")

# 1. Selectbox di Sidebar
pilihan_chart = st.sidebar.selectbox(
    "Pilih Jenis Grafik",
    ["Line Chart", "Bar Chart", "Area Chart"]
)

# 2. Slider di Sidebar
jumlah_data = st.sidebar.slider(
    "Jumlah Data (Baris)",
    min_value=10,
    max_value=100,
    value=30
)

# --- Logika Utama Aplikasi (Menggunakan Input Sidebar) ---
# Membuat data berdasarkan input slider
df = pd.DataFrame(
    np.random.randn(jumlah_data, 2),
    columns=['a', 'b']
)

st.header(f"Tampilan: {pilihan_chart} ({jumlah_data} Baris)")

if pilihan_chart == "Line Chart":
    st.line_chart(df)
elif pilihan_chart == "Bar Chart":
    st.bar_chart(df)
elif pilihan_chart == "Area Chart":
    st.area_chart(df)