import streamlit as st
import pandas as pd 
import numpy as np 

st.title("Notification Alert_Box")
st.write("Kelompok: 34")
st.markdown("""  
- Chika Karena - 0110222015  
- Chery Renata - 0110222011  
- Ira Pratiwi - 01102222162""")
# Judul halaman
st.title("Notification (Alert)")

# Menampilkan notifikasi sukses
st.success("✅ Data berhasil dimuat!")

# Menampilkan notifikasi informasi
st.info("ℹ️ Silakan periksa kembali data sebelum disimpan.")

# Menampilkan notifikasi peringatan
st.warning("⚠️ Beberapa data belum lengkap!")

# Menampilkan notifikasi error
st.error("❌ Terjadi kesalahan saat memproses data!")

# Menampilkan notifikasi exception (pesan kesalahan sistem)
try:
    x = 10 / 2
except Exception as e:
    st.exception(e)