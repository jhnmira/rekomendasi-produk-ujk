def filter_produk(data, kategori, budget):
    if budget == 0:
        hasil = data[data['kategori'] == kategori]
    else:
        hasil = data[
            (data['kategori'] == kategori) &
            (data['harga'] <= budget)
        ]
    return hasil
