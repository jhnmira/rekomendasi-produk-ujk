def filter_produk(data, kategori, budget):
    hasil = data[
        (data['kategori'] == kategori) &
        (data['harga'] <= budget)
    ]
    return hasil
