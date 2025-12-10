import streamlit as st
import matplotlib.pyplot as plt

# buat data sample
months = ['Jan', 'Feb','Mar','Apr','Mei', 'Jun', 'Jul', 'Aug','Sep','Oct', 'Nov', 'Des']
product_A_sales = [10,20,15,25,30,45,40,50,60,55,65,70]
product_B_sales = [5,10,8,15,18,20,22,30,25,35,40,45]

# Layout Streamlit
st.title("Virtualisasi Penjualan Produck")
st.sidebar.header("Pengaturan Grafik")
option = st.sidebar.selectbox("Pilih tipe virtualisasi  ") 




#identitas kelompk
st.caption("Praktikum 3 - Matplotlib Linechart")
st.markdown("""
Kelompok 32
Chika Karena - 0110222015
Chery Renata - 0110222011
Ira Pratiwi - 0110222162 
""", unsafe_allow_html=True)

# Single Line Plot
def line_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales, label='Product A')
    ax.set_title('Product Sales Over Months')
    ax.set_xlabel('Month')
    ax.set_ylabel('Sales')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

# Multiple Line Plot & Customizations
def customize_line_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales, label='Product A', color='blue', marker='o', linestyle='--')
    ax.plot(months, product_B_sales, label='Product B', color='red', marker='x', linestyle='-')

    ax.set_title('Product Sales Over Months')
    ax.set_xlabel('Month')
    ax.set_ylabel('Sales')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

# Jenis garis untuk menunjukan Trend
product_C_sales = [18,22,25,28,32,38,42,45,48,52,56,60]
product_D_sales = [7,9,11,13,16,18,20,23,25,28,30,33]
def tren_line_plot():
    fig, axs = plt.subplots()
    axs.plot(months, product_C_sales, label='Product C', color='green', linestyle='-.')
    axs.plot(months, product_D_sales, label='Product D', color='purple', linestyle=':')

    axs.set_title('Product Sales Trend Over Months')
    axs.set_xlabel('Month')
    axs.set_ylabel('Sales')
    axs.legend()
    axs.grid(True)
    st.pyplot(fig)

# Subplot
def subplot_line_plot():
    fig, axs = plt.subplots(2, 1, figsize=(10,8))
