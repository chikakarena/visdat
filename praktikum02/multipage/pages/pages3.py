import streamlit as st
import pandas as pd
import numpy as np

# --- Konten Halaman 3 ---
st.title("🗺️ Halaman 3: Map View")
st.markdown("Visualisasi data geospasial (Latitude & Longitude) menggunakan `st.map()`.")
# Identitas Kelompok
st.write("Kelompok: 04")
st.markdown("""
- Chika Karena - 0110222015
- Chery Renata - 0110222001
- Ira Pratiwi - 0110222162
""")
# 1. Membuat Data Lokasi Acak (sekitar wilayah Indonesia)
# Data: 50 pasang koordinat acak
# Offset: -6.2088 (Latitude Jakarta), 106.8456 (Longitude Jakarta)
df_lokasi = pd.DataFrame(
    np.random.randn(50, 2) / [100, 100] + [-6.2088, 106.8456], 
    columns=['latitude', 'longitude'] # Wajib bernama 'Latitude' dan 'Longitude'
)

# 2. Tampilkan Peta
st.map(df_lokasi)

st.caption("Peta menunjukkan 50 titik data acak yang terpusat di sekitar Jakarta.")