import streamlit as st
import pandas as pd
from utils.rekomendasi import filter_produk

st.set_page_config(page_title="Rekomendasi Produk", page_icon="💻")
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background-color: #f0f2f6;
}

.stButton > button {
    background-color: #4CAF50;
    color: white;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

st.title("💻 Sistem Rekomendasi Produk Elektronik")

data = pd.read_csv("data/produk.csv")

st.sidebar.header("Filter")

kategori = st.sidebar.selectbox("Kategori", data['kategori'].unique())
budget = st.sidebar.number_input("Budget", min_value=0)

if st.sidebar.button("Cari"):
    if budget == 0:
        st.warning("Masukkan budget terlebih dahulu")
    else:
        hasil = filter_produk(data, kategori, budget)
        hasil = hasil.sort_values(by="rating", ascending=False)

        if not hasil.empty:
            st.write("Hasil Rekomendasi:")
            hasil['harga'] = hasil['harga'].apply(lambda x: f"Rp {x:,.0f}")
            st.dataframe(hasil)
        else:
            st.warning("Tidak ada produk ditemukan")