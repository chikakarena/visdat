import streamlit as st

# --- Konfigurasi dan Identitas Kelompok ---
st.set_page_config(
    page_title="Praktikum Navigasi Multipage",
    layout="centered"
)

st.title("🏡 Halaman Utama (Main Page)")
st.header("Modul 2: Streamlit - 2")
st.markdown("""
Aplikasi ini mendemonstrasikan fitur **Multipage Navigation** Streamlit.
Setiap file di dalam folder `pages/` akan otomatis terdeteksi sebagai halaman baru.
""")

# Identitas Kelompok
st.write("Kelompok: 04")
st.markdown("""
- Chika Karena - 0110222015
- Chery Renata - 0110222001
- Ira Pratiwi - 0110222162
""")

st.info("Silakan gunakan menu di Sidebar untuk berpindah ke Page 2 atau Page 3.")