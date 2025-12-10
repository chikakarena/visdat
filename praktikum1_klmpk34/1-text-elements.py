#import library yang dibutuhkan
import streamlit as st

# BAGIAN 1 - text element
# header – untuk membuat tulisan header
st.header("ini header")
st.subheader("ini sub header")
st.text("ini teks biasa tanpa format") 
st.markdown("**ini teks bold** dan *ini teks italic*")
st.caption("ini caption")
st.markdown("""
ini baris 1  
ini menggunakan markdown multi baris  
ini baris 2  
ini menggunakan markdown multibaris  
ini baris 3  
ini menggunakan markdown multibaris
""")

# coba mandiri
# tuliskan :
# 1. Judul pakai praktikum pakai header
# 2. Bagian praktikum pakai subheader
# 3. Nama lengkap anggota + nim pakai markdown multibaris

st.header("Praktikum 1 Visualisasi Data")
st.subheader("Bagian 1: Teks Element")
st.markdown("""
1. Chika Karena - 0110222015
2. Chery Renata  - 0110222011
3. Ira Pratiwi - 01102222162

Kelas: VISUALISASI DATA (7TI01)  
Dosen Pengampu: Pak IMAM HAROMAIN, S.Si., M.Kom. 
STT Terpadu Nurul Fikri
""")


# ============================================================
# BAGIAN 2 - Menampilkan rumus (LaTeX)
# ============================================================

st.header("Displaying LaTeX")
st.latex(r'\cos^2\theta + \sin^2\theta = 1')  # rumus trigonometri
st.latex(r'(a+b)^2 = a^2 + b^2 + 2ab')        # rumus kuadrat binomial

# ============================================================
# BAGIAN 3 - Menampilkan kode program
# ============================================================

st.header("Displaying Code")
st.subheader("Python Code")

# Simpan ke variabel
code = '''
def hello():
    print("Hello, Streamlit!")
'''

st.code(code, language='python')

# ------------------------------------------------------------
# Java code
# ------------------------------------------------------------
st.subheader("Java Code")
st.code('''
public class GFG {
    public static void main(String[] args) {
        System.out.println("Hello World!");
    }
}
''', language='java')

# Fungsi st.code() bisa digunakan untuk bahasa pemrograman lain
# seperti Java, JavaScript, C++, HTML, DLL.

# ------------------------------------------------------------
# JavaScript code
# ------------------------------------------------------------
st.subheader("JavaScript Code")
st.code('''
<script>
try {
    alert("Welcome guest!"); // Kesalahan ketik (addaleert)
    addaleert("Ini error karena salah ketik!"); // sengaja dibuat untuk menimbulkan error
} catch(err) {
    document.getElementById("demo").innerHTML = err.message; 
    // menampilkan pesan error di elemen HTML dengan id 'demo'
}
</script>
''', language='javascript')

# Kode ini menunjukkan contoh bagaimana menangani error (exception) di JavaScript.
# Hasilnya tidak dijalankan di Streamlit, tapi ditampilkan sebagai contoh code.
