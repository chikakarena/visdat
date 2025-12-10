import streamlit as st
import time

# ============================================================
# IDENTITAS PRAKTIKUM
# ============================================================
st.header("Praktikum 1 Visualisasi Data")
st.subheader("Bagian 4: Buttons & Sliders (Interaktif)")
st.markdown("""
**Anggota Kelompok:**
1. Chika Karena – 0110222015  
2. Chery Renata – 0110222011  
3. Ira Pratiwi – 01102222162  

Kelas: VISUALISASI DATA (7TI01)  
Dosen Pengampu: Pak IMAM HAROMAIN, S.Si., M.Kom. 
STT Terpadu Nurul Fikri
""")

# ============================================================
# BUTTON
# ============================================================
st.subheader("1. Button")
if st.button("Klik ini untuk menampilkan pesan"):
    st.success(" sehat-sehat anak semester 7!")

# ============================================================
# RADIO BUTTON
# ============================================================
st.subheader("2. Radio Button")
pilihan_bahasa = st.radio(
    "Pilih bahasa pemrograman favorit:",
    ("Python", "Java", "C++")
)
st.write("Bahasa yang kamu pilih adalah:", pilihan_bahasa)

# ============================================================
# CHECKBOX
# ============================================================
st.subheader("3. Checkbox")
if st.checkbox("Tampilkan informasi tambahan"):
    st.info("Checkbox sedang aktif ✅")

# ============================================================
# SELECTBOX
# ============================================================
st.subheader("4. SelectBox (Dropdown)")
jurusan = st.selectbox(
    "Pilih Program Studi:",
    ["Teknik Informatika", "Sistem Informasi", "Bisnis Digital"]
)
st.write("Program studi yang dipilih:", jurusan)

# ============================================================
# MULTISELECT
# ============================================================
st.subheader("5. Multiselect")
hobi = st.multiselect(
    "Pilih hobi:",
    ["Membaca", "Ngoding", "Gaming", "Traveling", "Nonton film"]
)
st.write("Hobimu adalah:", hobi)

# ============================================================
# SLIDER
# ============================================================
st.subheader("6. Slider")
nilai = st.slider("Atur nilai:", 0, 100, 50)
st.write("Nilai yang dipilih:", nilai)

# ============================================================
# DOWNLOAD BUTTON
# ============================================================
st.subheader("7. Download Button")
st.download_button(
    label="Download File chika,ira,chery",
    data="chika,ira,chery.",
    file_name="cic.txt"
)

# ============================================================
# PROGRESS BAR & SPINNER
# ============================================================
st.subheader("8. Progress Bar & Spinner (Loading Process)")

if st.button("Mulai proses loading"):
    with st.spinner("Sedang memproses..."):
        progress = st.progress(0)
        for i in range(100):
            time.sleep(0.02)
            progress.progress(i + 1)
    st.success("Proses selesai ✅")
