# menghitung bunga per bulan
def Bunga_Per_Bulan (Bunga_Tahunan, Jumlah_Pinjaman):
    return (Bunga_Tahunan/12)*Jumlah_Pinjaman

# menghitung cicilan per bulan 
def Cicilan_Per_Bulan (Jumlah_Pinjaman, Bunga_Per_Bulan, Jumlah_Bulan):
    return (Jumlah_Pinjaman+Bunga_Per_Bulan)/Jumlah_Bulan

# input data
Nama = input("Masukkan Nama: ")
NIM = input ("Masukkan NIM: ")
Jumlah_Pinjaman = 17000000

# opsi lama cicilan
print("\nPilih Lama Cicilan: ")
print("1. 1 tahun")
print("2. 2 tahun")
print("3. 3 tahun")

Lama_Cicilan = int(input("Masukkan Pilihan Lama Cicilan (1,2, atau 3): "))

# lama cicilan yang dipilih 
if Lama_Cicilan == 1 :
    Bunga_Tahunan = 0.07
    Bunga_Per_Bulan = Bunga_Per_Bulan (Bunga_Tahunan, Jumlah_Pinjaman)
    Jumlah_Bulan = 12
elif Lama_Cicilan == 2 :
    Bunga_Tahunan = 0.13
    Bunga_Per_Bulan = Bunga_Per_Bulan (Bunga_Tahunan, Jumlah_Pinjaman)
    Jumlah_Bulan = 24
elif Lama_Cicilan == 3 :
    Bunga_Tahunan = 0.19
    Bunga_Per_Bulan = Bunga_Per_Bulan (Bunga_Tahunan, Jumlah_Pinjaman)
    Jumlah_Bulan = 36
else:
    print("Pilihan tidak valid")
    exit ( )

# total cicilan per bulan
Total_Cicilan_Per_Bulan = Cicilan_Per_Bulan (Jumlah_Pinjaman, Bunga_Per_Bulan, Jumlah_Bulan)

# output hasil
print(f"\nNama: {Nama}")
print(f"NIM: {NIM}")
print(f"Jumlah Pinjaman: Rp{Jumlah_Pinjaman}")
print(f"Lama Cicilan: {Jumlah_Bulan} Bulan")
print(f"Total Cicilan Per Bulan: Rp{Total_Cicilan_Per_Bulan: 2f}")