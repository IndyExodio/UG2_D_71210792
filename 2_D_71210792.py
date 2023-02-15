nomor = input("Masukkan Nomor Telepon : ")

if nomor[:4] == "0816":
    # operator = "Indosat"
    print("Anda menggunakan operator Indosat")
elif nomor[:4] == "0814":
    # operator = "Telkomsel"
    print("Anda menggunakan operator Telkomsel")
else:
    print("Operator anda tidak diketahui")
        
angka_terakhir = int(nomor[-1])
if angka_terakhir % 2 == 0:
    ganjil_genap = "genap"
else:
    ganjil_genap = "ganjil"
        
print("Nomor anda berakhiran", ganjil_genap)