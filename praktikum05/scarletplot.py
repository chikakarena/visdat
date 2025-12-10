import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Dataset
suhu = [20, 22, 24, 26, 28, 30, 32, 34, 36]
penjualan = [50, 60, 70, 90, 100, 110, 130, 150, 180]

#Dataset Tambahan

# Data tambahan untuk kategori hari
penjualan_weekdays = [50, 60, 70, 80, 90, 100, 110, 120, 130]
penjualan_weekend = [60, 70, 80, 100, 110, 120, 140, 160, 200]


# data untuk analisis
data = {
    'Suhu': [20, 22, 24, 26, 28, 30, 32, 34, 36],
    'Penjualan_Cokelat': [40, 45, 50, 55, 60, 65, 70, 75, 80],
    'Penjualan_Vanila': [82, 80, 78, 76, 77, 80, 82, 85, 88],
    'Penjualan_Stroberi': [55, 50, 55, 60, 65, 66, 70, 72, 75],
    'Kelembapan': [50, 65, 70, 75, 80, 85, 90, 95, 100]
}
# konversi ke dataframe
df = pd.DataFrame(data)
# layout utama
st.title('Visualisasi Scatter Plot Penjualan Es Krim')
st.sidebar.header("Pengaturan Visualisasi")

# Menu di Sidebar
option = st.sidebar.selectbox(
    "Pilih contoh scatter plot",
    (
        "Basic Scatter Plot",
        "Kustomisasi Scatter Plot",
        "Multiple Scatter Plot",
        "Analisis Scatter Plot"
    )
)

# Identitas Kelompok
st.caption("Praktikum 5 - Matplotlib Scatter Plot")
st.markdown("Kelompok 2")
st.write("Nama Lengkap Anggota 1 - NIM")
st.write("Nama Lengkap Anggota 2 - NIM")
st.write("Nama Lengkap Anggota 3 - NIM")
st.write("Nama Lengkap Anggota 4 - NIM")
st.write("Nama Lengkap Anggota 5 - NIM")

# 1. Basic Scatter Plot
def basic_scatter():
    st.subheader('1. Basic Scatter Plot')
    fig, ax = plt.subplots()
    ax.scatter(df['Suhu'], df['Penjualan_Cokelat'])
    ax.set_title('Hubungan Penjualan Es Krim dengan Suhu')
    ax.set_xlabel('Suhu')
    ax.set_ylabel('Penjualan Es Krim')
    st.pyplot(fig)

# 2. Kustomisasi Scatter Plot
def customized_scatter():
    st.subheader('2. Kustomisasi Scatter Plot')
    fig, ax = plt.subplots()
    ax.scatter(df['Suhu'], df['Penjualan_Cokelat'])
    ax.set_title('Hubungan Penjualan Es Krim dengan Suhu')
    ax.set_xlabel('Suhu')
    ax.set_ylabel('Penjualan Es Krim')
    st.pyplot(fig)

# 3. Multiple Scatter Plot
# 3. Multiple Scatter Plot
def multiple_scatter():
    st.subheader('3. Multiple Scatter Plot')
    fig, ax = plt.subplots()
    
    # Scatter plot untuk Hari Kerja
    ax.scatter(suhu, penjualan_weekdays, color='green', label='Hari Kerja', s=80)
    
    # Scatter plot untuk Akhir Pekan
    ax.scatter(suhu, penjualan_weekend, color='purple', label='Akhir Pekan', s=80)
    
    ax.set_title('Hubungan Penjualan Es Krim dengan Suhu')
    ax.set_xlabel('Suhu')
    ax.set_ylabel('Penjualan Es Krim')
    
    ax.legend() # Menambahkan legenda untuk membedakan Hari Kerja dan Akhir Pekan
    ax.grid(True)
    st.pyplot(fig)

# 4. Analisis dengan Scatter Plot
def scatter_3_variabel():
    st.subheader('4. Analisis dengan Scatter Plot')
    
    # Menampilkan opsi pemilihan jenis es krim di antarmuka Streamlit
    jenis_eskrim = st.selectbox(
        'Pilih Jenis Es Krim', 
        ['Cokelat', 'Vanila', 'Stroberi']
    )
    
# logika untuk opsi jenis eskrim berdasarkan pilihan
    if jenis_eskrim == 'Cokelat':
        penjualan = df['Penjualan_Cokelat']
    elif jenis_eskrim == 'Vanila':
        penjualan = df['Penjualan_Vanila']
    else: # Ini mencakup pilihan 'Stroberi' jika yang lain tidak dipilih
        penjualan = df['Penjualan_Stroberi']

st.subheader("Data Penjualan dan Suhu")
st.dataframe(df)

# scatter plot
fig, ax = plt.subplots()
# Asumsi: df['Suhu'] dan penjualan sudah didefinisikan sebelumnya.
# Asumsi: df['Kelembapan'] adalah variabel ketiga untuk color mapping.
scatter = ax.scatter(df['Suhu'], penjualan, c=df['Kelembapan'], s=100, cmap='coolwarm', alpha=0.7)

# styling
ax.title('Hubungan Penjualan, Suhu, dan Kelembapan')
ax.xlabel('Suhu')
ax.ylabel('Penjualan Es Krim')
fig.colorbar(scatter, label='Kelembaban (%)')

st.pyplot(fig)
# ringkasan hubungan
st.subheader('Analisis Hubungan')
st.write(f'Grafik menunjukkan hubungan antara suhu, kelembaban, dan penjualan eskrim jenis *(jenis_eskrim)*.')
# Routing berdasarkan menu sidebar
if option == 'Basic Scatter Plot':
    basic_scatter()
elif option == 'Kustomisasi Scatter Plot':
    customized_scatter() 
elif option == 'Multiple Scatter Plot':
    multiple_scatter()
elif option == 'Analisis dengan Scatter Plot':
    scatter_3_variabel() 


