import streamlit as st
import pandas as pd
from utils.rekomendasi import filter_produk

st.set_page_config(page_title="Rekomendasi Produk", page_icon="💻")

st.title("💻 Sistem Rekomendasi Produk Elektronik")

st.info("Silakan pilih kategori dan masukkan budget, lalu klik tombol Cari")

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
            st.subheader("Hasil Rekomendasi")
            st.success(f"Ditemukan {len(hasil)} produk")
            hasil['harga'] = hasil['harga'].apply(lambda x: f"Rp {x:,.0f}")
            st.dataframe(hasil)
        else:
            st.warning("Tidak ada produk ditemukan")
