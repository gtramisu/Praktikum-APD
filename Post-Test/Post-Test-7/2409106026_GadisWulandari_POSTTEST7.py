admin = [["gadis", "gadis26", "admin"]]
minuman = {
    "Kopi Kenangan Mantan": {"deskripsi": "Kopi susu dengan gula aren", "harga": {"R": 18000, "L": 24000}},
    "Matcha Latte": {"deskripsi": "Matcha yang otentik dengan susu segar", "harga": {"R": 28000, "L": 38000}},
    "Hojicha Latte": {"deskripsi": "Perpaduan antara teh Jepang dan kopi", "harga": {"R": 24000, "L": 29000}},
    "Earl Grey Tea": {"deskripsi": "Teh hitam dengan ekstrak kulit buah bergamot", "harga": {"R": 15000, "L": 19000}},
    "Milk Tea Boba": {"deskripsi": "Teh susu dengan topping boba", "harga": {"R": 25000, "L": 29000}},
    "Milo Dinosaurus": {"deskripsi": "Coklat malt yang unik dengan tumpukan bubuk Milo", "harga": {"R": 22000, "L": 29000}},
    "Magic Spanish Latte": {"deskripsi": "Susu yang creamy dengan espresso", "harga": {"R": 19000, "L": 25000}}
}
pesanan = []
riwayat_pesanan = []

def tampilkan_minuman():
    print("="*95)
    print("Daftar Minuman: ".center(95))
    print("="*95)
    for idx, drink in enumerate(minuman.keys(), start=1):
        print(f"{idx}. {drink} (R: Rp{minuman[drink]['harga']['R']}, L: Rp{minuman[drink]['harga']['L']}) - {minuman[drink]['deskripsi']}")
    print("="*95)

def tambah_pesanan(nama_pembeli):
    while True:
        tampilkan_minuman()
        minuman_pilihan = input("\nPilih minuman (nomor): ")
        if minuman_pilihan.isdigit():
            minuman_pilihan = int(minuman_pilihan) - 1
            if 0 <= minuman_pilihan < len(minuman):
                drink_name = list(minuman.keys())[minuman_pilihan]
                ukuran = input("Masukkan ukuran minuman (R/L): ").upper()
                if ukuran in minuman[drink_name]['harga']:
                    harga = minuman[drink_name]['harga'][ukuran]
                    pesanan.append([nama_pembeli, drink_name, harga, ukuran])
                    print("Pesanan berhasil ditambahkan!\n")
                    break
                else:
                    print("Ukurannya tidak valid!\n")
            else:
                print("Minumannya tidak ada!\n")
        else:
            print("Pilihan harus menggunakan angka yaa\n")

def hitung_total_harga():
    total_harga = 0
    for order in pesanan:
        total_harga += order[2]
    return total_harga

def konfirmasi_pesanan():
    if not pesanan:
        print("Tidak ada pesanan yang dibuat.\n")
        return
    print("Pesanan Anda: \n")
    for order in pesanan:
        print(f"Nama Pembeli: {order[0]}, Minuman: {order[1]}, Harga: Rp{order[2]}, Ukuran: {order[3]}")
    total_harga = hitung_total_harga()
    print(f"Total Harga Pesanan: Rp{total_harga}")
    
    konfirmasi = input("\nKamu yakin mau beli ini saja? (ya/tidak): ").lower()
    if konfirmasi == 'ya':
        print("="*50)
        print("Pesanan anda berhasil dan sedang dibuat".center(50))
        print("Silahkan tunggu yaa".center(50))
        print("="*50)
        pesanan.clear()
    else:
        print("Yahh pesanannya dibatalkan\n")

def edit_pesanan(nama_pembeli):
    ditemukan = False
    for order in pesanan:
        if order[0] == nama_pembeli:
            print("\nPesanan saat ini: ", order)
            tampilkan_minuman()
            minuman_pilihan = input("\nPilih minuman baru (nomor): ")
            if minuman_pilihan.isdigit():
                minuman_pilihan = int(minuman_pilihan) - 1
                if 0 <= minuman_pilihan < len(minuman):
                    drink_name = list(minuman.keys())[minuman_pilihan]
                    ukuran = input("Masukkan ukuran minuman baru (R/L): ").upper()
                    if ukuran in minuman[drink_name]['harga']:
                        harga = minuman[drink_name]['harga'][ukuran]
                        order[1] = drink_name
                        order[2] = harga
                        order[3] = ukuran
                        print("Pesanan berhasil diedit\n")
                        ditemukan = True
                        break
                    else:
                        print("Ukurannya tidak valid!\n")
                else:
                    print("Minumannya tidak ada!\n")
    if not ditemukan:
        print("Yahh pesanan tidak ditemukan\n")

def hapus_pesanan(nama_pembeli):
    ditemukan = False
    for order in pesanan:
        if order[0] == nama_pembeli:
            print("Pesanan saat ini: ", order)
            konfirmasi = input("Kamu yakin ingin menghapus pesanan ini? (ya/tidak): ").lower()
            if konfirmasi == 'ya':
                pesanan.remove(order)
                riwayat_pesanan.append(order)
                print("Pesanan berhasil dihapus!\n")
                ditemukan = True
                break
            else:
                print("Pesanan tidak jadi dihapus.\n")
    if not ditemukan:
        print("Yahh pesanan tidak ditemukan\n")

def lihat_pesanan(nama_pembeli):
    ditemukan = False
    for order in pesanan:
        if order[0] == nama_pembeli:
            print(f"Nama Pembeli: {order[0]}, Minuman: {order[1]}, Harga: Rp{order[2]}, Ukuran: {order[3]}")
            ditemukan = True
    if not ditemukan:
        print("Tidak ada pesanan untuk nama ini.\n")

print("="*65)
print("Halo, selamat datang di Kopi Kenangan!".center(65))
print("Jika belum punya akun, silahkan registrasi terlebih dahulu yaa".center(65))
print("="*65)

pengguna = None
while pengguna is None:
    print("1. Login")
    print("2. Registrasi")
    pilih = input("Pilih opsi (1/2): ")
    if pilih == '1':
        username = input("\nUsername: ")
        password = input("Password: ")
        for i in admin:
            if i[0] == username and i[1] == password:
                pengguna = i
                break
        if pengguna is None:
            print("Username atau password salah nih\n")
    elif pilih == '2':
        username = input("Buat username baru: ")
        password = input("Buat password baru: ")
        admin.append([username, password, 'user'])
        print("Yeyyy registrasi berhasil! Kamu bisa login sekarang\n")
    else:
        print("Pilihan tidak valid!\n")

if pengguna[2] == 'admin':
    while True:
        print("="*60)
        print(
        """
        ===================================
        |       KASIR KOPI KENANGAN       |
        =================================== 
        |        1. TAMBAH PESANAN        |          
        |        2. EDIT PESANAN          |          
        |        3. HAPUS PESANAN         |     
        |        4. LIHAT PESANAN         |
        |        5. PESAN                 |      
        |        6. LOGOUT                |  
        ===================================
        """
        )
        pilih = input("Pilih opsi (1-6): ")

        if pilih == '1':
            nama_pembeli = input("Masukkan nama pembeli: ")
            tambah_pesanan(nama_pembeli)

        elif pilih == '2':
            nama_pembeli = input("Masukkan nama pembeli yang pesanan mau diedit: ")
            edit_pesanan(nama_pembeli)

        elif pilih == '3':
            nama_pembeli = input("Masukkan nama pembeli yang pesanan ingin dihapus: ")
            hapus_pesanan(nama_pembeli)

        elif pilih == '4':
            nama_pembeli = input("Masukkan nama pembeli untuk melihat pesanan: ")
            lihat_pesanan(nama_pembeli)

        elif pilih == '5':  
            konfirmasi_pesanan()
            break

        elif pilih == '6':
            print("Logout berhasil, terimakasih!\n")
            break
        else:
            print("Pilihan tidak valid!\n")

else:
    while True:
        print("="*60)
        print(
        """
        ===================================
        |       KASIR KOPI KENANGAN       |
        =================================== 
        |        1. TAMBAH PESANAN        |          
        |        2. LIHAT PESANAN         |          
        |        3. PESAN                 |      
        |        4. LOGOUT                |  
        ===================================
        """
        )
        pilih = input("Pilih opsi (1-4): ")

        if pilih == '1':
            nama_pembeli = input("Masukkan nama pembeli: ")
            tambah_pesanan(nama_pembeli)

        elif pilih == '2':
            nama_pembeli = input("Masukkan nama pembeli untuk melihat pesanan: ")
            lihat_pesanan(nama_pembeli)

        elif pilih == '3':  
            konfirmasi_pesanan()
            break

        elif pilih == '4':
            print("Logout berhasil, terimakasih!\n")
            break
        else:
            print("Pilihan tidak valid!\n")
 