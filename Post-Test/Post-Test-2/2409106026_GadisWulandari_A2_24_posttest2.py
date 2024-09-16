nama = input("Masukkan nama lengkap Anda: ")
nim = input("Masukkan NIM Anda: ")
harga_beras = float(input("Masukkan harga beras: "))

diskon_mawar = 11 / 100
diskon_sania = 14 / 100
diskon_maknyus = 17 / 100

harga_setelah_diskon_mawar = harga_beras - (harga_beras * diskon_mawar)
harga_setelah_diskon_sania = harga_beras - (harga_beras * diskon_sania)
harga_setelah_diskon_maknyus = harga_beras - (harga_beras * diskon_maknyus)

print(f"{nama} dengan NIM {nim} ingin membeli beras seharga Rp {harga_beras}")
print(f"Jika dia membeli beras Mawar, ia harus membayar Rp {harga_setelah_diskon_mawar:.2f} setelah mendapat diskon 11%.")
print(f"Jika dia membeli beras Sania, ia harus membayar Rp {harga_setelah_diskon_sania:.2f} setelah mendapat diskon 14%.")
print(f"Jika dia membeli beras Maknyus, ia harus membayar Rp {harga_setelah_diskon_maknyus:.2f} setelah mendapat diskon 17%.")