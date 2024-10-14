admin = {"gadis": ["gadis26", "admin"]}

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

print("="*65)
print("haloo selamat datang di Kopi Kenangan!".center(65))
print("jika belum punya akun, silahkan registrasi terlebih dahulu yaa".center(65))
print("="*65)

pengguna = None
while pengguna is None:
    print("1. Login")
    print("2. Registrasi")
    pilih = input("Pilih opsi (1/2): ")
    if pilih == '1':
        username = input("\nUsername: ")
        password = input("Password: ")
        if username in admin and admin[username][0] == password:
            pengguna = [username, password, admin[username][1]]
        else:
            print("username atau password salah nih\n")
    elif pilih == '2':
        username = input("Buat username baru: ")
        password = input("Buat password baru: ")
        admin[username] = [password, 'user']

        print("yeyyy registrasi berhasil!")
        print("kamu bisa login sekarang\n")
    else:
        print("pilihan tidak valid!\n")

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
            print("="*95)
            print("Daftar Minuman: ".center(95))
            print("="*95)
            for idx, drink in enumerate(minuman.keys(), start=1):
                print(f"{idx}. {drink} (R: Rp{minuman[drink]['harga']['R']}, L: Rp{minuman[drink]['harga']['L']}) - {minuman[drink]['deskripsi']}")
            print("="*95)
            minuman_pilihan = input("\nPilih minuman (nomor): ")
            if minuman_pilihan.isdigit():
                minuman_pilihan = int(minuman_pilihan) - 1
                if 0 <= minuman_pilihan < len(minuman):
                    minuman_pilihan = list(minuman.keys())[minuman_pilihan]
                    ukuran = input("Masukkan ukuran minuman (R/L): ").upper()
                    if ukuran in minuman[minuman_pilihan]['harga']:
                        harga = minuman[minuman_pilihan]['harga'][ukuran]
                        pesanan.append([nama_pembeli, minuman_pilihan, harga, ukuran])
                        print("pesanan kamu berhasil ditambahkan!\n")
                    else:
                        print("ukurannya tidak valid!\n")
                else:
                    print("minumannya tidak adaa!\n")
            else:
                print("pilihan harus pake angka yaa\n")

        elif pilih == '2':
            nama_pembeli = input("Masukkan nama pembeli yang pesanannya mau diedit: ")
            ditemukan = False
            for order in pesanan:
                if order[0] == nama_pembeli:
                    print("\nPesanan saat ini: ", order)
                    print("="*95)
                    print("Daftar Minuman: ".center(95))
                    print("="*95)
                    for idx, drink in enumerate(minuman.keys(), start=1):
                        print(f"{idx}. {drink} (R: Rp{minuman[drink]['harga']['R']}, L: Rp{minuman[drink]['harga']['L']}) - {minuman[drink]['deskripsi']}")
                    print("="*95)
                    minuman_pilihan = input("\nPilih minuman baru (nomor): ")
                    if minuman_pilihan.isdigit():
                        minuman_pilihan = int(minuman_pilihan) - 1
                        if 0 <= minuman_pilihan < len(minuman):
                            minuman_pilihan = list(minuman.keys())[minuman_pilihan]
                            ukuran = input("Masukkan ukuran minuman baru (R/L): ").upper()
                            if ukuran in minuman[minuman_pilihan]['harga']:
                                harga = minuman[minuman_pilihan]['harga'][ukuran]
                                order[1] = minuman_pilihan
                                order[2] = harga
                                order[3] = ukuran
                                print("okeii pesanan kamu berhasil diedit\n")
                                ditemukan = True
                                break
                            else:
                                print("ukurannya tidak valid!\n")
                        else:
                            print("minumannya tidak adaa!\n")
            if not ditemukan:
                print("yahh pesanan tidak ditemukan\n")

        elif pilih == '3':
            nama_pembeli = input("Masukkan nama pembeli yang pesanannya ingin dihapus: ")
            ditemukan = False
            for order in pesanan:
                if order[0] == nama_pembeli:
                    print("Pesanan saat ini: ", order)
                    konfirmasi = input("kamu yakin ingin menghapus pesanan ini? (ya/tidak): ").lower()
                    if konfirmasi == 'ya':
                        pesanan.remove(order)
                        riwayat_pesanan.append(order)
                        print("pesanan berhasil dihapus!\n")
                    else:
                        print("pesanan gajadi dihapus yeyy")
                    ditemukan = True
                    break
            if not ditemukan:
                print("yahh pesanan tidak ditemukan\n")

        elif pilih == '4':
            if not pesanan:
                print("tidak ada pesanan kamu saat ini.\n")
            else:
                print("Daftar Pesanan: \n")
                for order in pesanan:
                    print(f"Nama Pembeli: {order[0]}, Minuman: {order[1]}, Harga: Rp{order[2]}, Ukuran: {order[3]}")
                print()

        elif pilih == '5':  
            print("Pesanan Anda: \n")
            if not pesanan: 
                print("Tidak ada pesanan yang dibuat.\n")
            else:
                total_harga = 0  
                for order in pesanan: 
                    print(f"Nama Pembeli: {order[0]}, Minuman: {order[1]}, Harga: Rp{order[2]}, Ukuran: {order[3]}")
                    total_harga += order[2]  

                print(f"Total Harga Pesanan: Rp{total_harga}")  
        
            konfirmasi = input("\nKamu yakin mau beli ini saja? (ya/tidak): ").lower()
            if konfirmasi == 'ya':
                print("="*50)
                print("Pesanan anda berhasil dan sedang dibuat".center(50))
                print("Silahkan tunggu yaa".center(50))
                print("="*50)
                pesanan.clear() 
                break 
            else:
                print("Yahh pesanannya dibatalkan\n")

        elif pilih == '6':
            print("logout berhasil, terimakasih!\n")
            break
        else:
            print("pilihan tidak valid!\n")

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
            print("="*95)
            print("Daftar Minuman: ".center(95))
            print("="*95)
            for idx, drink in enumerate(minuman.keys(), start=1):
                print(f"{idx}. {drink} (R: Rp{minuman[drink]['harga']['R']}, L: Rp{minuman[drink]['harga']['L']}) - {minuman[drink]['deskripsi']}")
            print("="*95)
            minuman_pilihan = input("\nPilih minuman (nomor): ")
            if minuman_pilihan.isdigit():
                minuman_pilihan = int(                minuman_pilihan) - 1
                if 0 <= minuman_pilihan < len(minuman):
                    minuman_pilihan = list(minuman.keys())[minuman_pilihan]
                    ukuran = input("Masukkan ukuran minuman (R/L): ").upper()
                    if ukuran in minuman[minuman_pilihan]['harga']:
                        harga = minuman[minuman_pilihan]['harga'][ukuran]
                        pesanan.append([nama_pembeli, minuman_pilihan, harga, ukuran])
                        print("Pesanan berhasil ditambahkan!\n")
                    else:
                        print("Ukurannya tidak valid!\n")
                else:
                    print("Minumannya tidak ada!\n")
            else:
                print("Pilihan harus pake angka yaa\n")

        elif pilih == '2':
            if not pesanan:
                print("Tidak ada pesanan kamu saat ini.\n")
            else:
                print("Daftar Pesanan: \n")
                for order in pesanan:
                    print(f"Nama Pembeli: {order[0]}, Minuman: {order[1]}, Harga: Rp{order[2]}, Ukuran: {order[3]}")
                print()

        elif pilih == '3':  
            print("Pesanan Anda: \n")
            if not pesanan: 
                print("Tidak ada pesanan yang dibuat.\n")
            else:
                total_harga = 0  
                for order in pesanan: 
                    print(f"Nama Pembeli: {order[0]}, Minuman: {order[1]}, Harga: Rp{order[2]}, Ukuran: {order[3]}")
                    total_harga += order[2]  

                print(f"Total Harga Pesanan: Rp{total_harga}")  
        
            konfirmasi = input("\nKamu yakin mau beli ini saja? (ya/tidak): ").lower()
            if konfirmasi == 'ya':
                print("="*50)
                print("Pesanan anda berhasil dan sedang dibuat".center(50))
                print("Silahkan tunggu yaa".center(50))
                print("="*50)
                pesanan.clear() 
                break 
            else:
                print("Yahh pesanannya dibatalkan\n")

        elif pilih == '4':
            print("Logout berhasil, terimakasih!\n")
            break
        else:
            print("Pilihan tidak valid!\n")
 

            