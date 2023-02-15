nama_barang = input("Masukkan nama barang : ")
harga_barang = int(input("Masukkan harga barang : "))

if harga_barang >= 25000000:
    diskon = 0.25 * harga_barang
elif harga_barang >= 10000000:
    diskon = 0.1 * harga_barang
else:
    diskon = 0

print("Nama Barang: ", nama_barang)
print("Harga Barang: Rp", harga_barang)
print("Diskon: Rp", diskon)

total_diskon = diskon

jumlah_bayar = harga_barang - diskon
print("Total Diskon: Rp", total_diskon)
print("Jumlah yang harus dibayarkan: Rp", jumlah_bayar)
