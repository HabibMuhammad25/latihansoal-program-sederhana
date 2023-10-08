# Soal Pertama
print('=' * 30)
print('        Toko Nusantara          ')
print('=' * 30)

# Proses input User
harga = eval(input("Masukkan Harga Barang : Rp. "))
jumlah = eval(input("Masukkan Jumlah Barang : "))

# Proses Output
print()
total = harga * jumlah
print("Total Harga = ", "Rp. ", total)
print()

bayar = eval(input("Masukkan Jumlah Uang : Rp. "))
kembalian = (bayar - total)
print("Uang kembalian = ", "Rp.", kembalian)
print()