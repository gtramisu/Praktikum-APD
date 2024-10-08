admin = [["gadis", "gadis26", "admin"]]

minuman = [
    ["Kopi Kenangan Mantan", "Kopi susu dengan gula aren", {"R": 18000, "L": 24000}],
    ["Matcha Latte", "Matcha yang otentik dengan susu segar", {"R": 28000, "L": 38000}],
    ["Hojicha Latte", "Perpaduan antara teh Jepang dan kopi", {"R": 24000, "L": 29000}],
    ["Earl Grey Tea", "Teh hitam dengan ekstrak kulit buah bergamot", {"R": 15000, "L": 19000}],
    ["Milk Tea Boba", "Teh susu dengan topping boba", {"R": 25000, "L": 29000}],
    ["Milo Dinosaurus", "Coklat malt yang unik dengan tumpukan bubuk Milo", {"R": 22000, "L": 29000}],
    ["Magic Spanish Latte", "Susu yang creamy dengan espresso", {"R": 19000, "L": 25000}]
]

pesanan = []
riwayat_pesanan = []

print("haloo selamat datang di Kopi Kenangan!\n")
print("jika belum punya akun, silahkan registrasi terlebih dahulu yaa\n")

pengguna = None
while pengguna is None:
    print("1. Login")
    print("2. Registrasi")
    pilih = input("Pilih opsi (1/2): ")
    if pilih == '1':
        username = input("Username: ")
        password = input("Password: ")
        for i in admin:
            if i[0] == username and i[1] == password:
                pengguna = i
                break
        if pengguna is None:
            print("username atau password salah nih\n")
    elif pilih == '2':
        username = input("Buat username baru: ")
        password = input("Buat password baru: ")
        admin.append([username, password, 'user'])

        print("yeyyy registrasi berhasil!")
        print("kamu bisa login sekarang\n")
    else:
        print("pilihan tidak valid!\n")

if pengguna[2] == 'admin':
    while True:
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
            print("Daftar Minuman: ")
            for idx, drink in enumerate(minuman, start=1):
                print(f"{idx}. {drink[0]} (R: Rp{drink[2]['R']}, L: Rp{drink[2]['L']}) - {drink[1]}")
            minuman_pilihan = input("Pilih minuman (nomor): ")
            if minuman_pilihan.isdigit():
                minuman_pilihan = int(minuman_pilihan) - 1
                if 0 <= minuman_pilihan < len(minuman):
                    ukuran = input("Masukkan ukuran minuman (R/L): ").upper()
                    if ukuran in minuman[minuman_pilihan][2]:
                        harga = minuman[minuman_pilihan][2][ukuran]
                        pesanan.append([nama_pembeli, minuman[minuman_pilihan][0], harga, ukuran])
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
                    print("Pesanan saat ini: ", order)
                    print("Daftar Minuman: ")
                    for idx, drink in enumerate(minuman, start=1):
                        print(f"{idx}. {drink[0]} (R: Rp{drink[2]['R']}, L: Rp{drink[2]['L']}) - {drink[1]}")
                    minuman_pilihan = input("Pilih minuman baru (nomor): ")
                    if minuman_pilihan.isdigit():
                        minuman_pilihan = int(minuman_pilihan) - 1
                        if 0 <= minuman_pilihan < len(minuman):
                            ukuran = input("Masukkan ukuran minuman baru (R/L): ").upper()
                            if ukuran in minuman[minuman_pilihan][2]:
                                harga = minuman[minuman_pilihan][2][ukuran]
                                order[1] = minuman[minuman_pilihan][0]
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
                print("Daftar Pesanan: ")
                for order in pesanan:
                    print(f"Nama Pembeli: {order[0]}, Minuman: {order[1]}, Harga: Rp{order[2]}, Ukuran: {order[3]}")
                print()

        elif pilih == '5':  
            print("Pesanan Anda: ")
            if not pesanan: 
                print("Tidak ada pesanan yang dibuat.\n")
            else:
                total_harga = 0  
                for order in pesanan: 
                    print(f"Nama Pembeli: {order[0]}, Minuman: {order[1]}, Harga: Rp{order[2]}, Ukuran: {order[3]}")
                    total_harga += order[2]  

                    print(f"Total Harga Pesanan: Rp{total_harga}")  
        
            konfirmasi = input("Kamu yakin mau beli ini saja? (ya/tidak): ").lower()
            if konfirmasi == 'ya':
                print("Pesanan anda berhasil dan sedang dibuat, silahkan tunggu yaa!\n")
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
            print("Daftar Minuman: ")

            for idx, drink in enumerate(minuman, start=1):
                print(f"{idx}. {drink[0]} (R: Rp{drink[2]['R']}, L: Rp{drink[2]['L']}) - {drink[1]}")
            minuman_pilihan = input("Pilih minuman (nomor): ")
            if minuman_pilihan.isdigit():
                minuman_pilihan = int(minuman_pilihan) - 1
                if 0 <= minuman_pilihan < len(minuman):
                    ukuran = input("Masukkan ukuran minuman (R/L): ").upper()
                    if ukuran in minuman[minuman_pilihan][2]:
                        harga = minuman[minuman_pilihan][2][ukuran]
                        pesanan.append([nama_pembeli, minuman[minuman_pilihan][0], harga, ukuran])
                        print("Pesanan berhasil ditambahkan!\n")
                    else:
                        print("Ukurannya tidak valid!\n")
                else:
                    print("minumannya tidak adaa!\n")
            else:
                print("pilihan harus pake angka yaa\n")

        elif pilih == '2':
            if not pesanan:
                print("tidak ada pesanan kamu saat ini.\n")
            else:
                print("Daftar Pesanan: ")
                for order in pesanan:
                    print(f"Nama Pembeli: {order[0]}, Minuman: {order[1]}, Harga: Rp{order[2]}, Ukuran: {order[3]}")
                print()

        elif pilih == '3':  
            print("Pesanan Anda: ")
            if not pesanan: 
                print("Tidak ada pesanan yang dibuat.\n")
            else:
                total_harga = 0  
                for order in pesanan: 
                    print(f"Nama Pembeli: {order[0]}, Minuman: {order[1]}, Harga: Rp{order[2]}, Ukuran: {order[3]}")
                    total_harga += order[2]  

                    print(f"Total Harga Pesanan: Rp{total_harga}")  
        
            konfirmasi = input("Kamu yakin mau beli ini saja? (ya/tidak): ").lower()
            if konfirmasi == 'ya':
                print("Pesanan anda berhasil dan sedang dibuat, silahkan tunggu yaa!\n")
                pesanan.clear() 
                break 
            else:
                print("Yahh pesanannya dibatalkan\n")

        elif pilih == '4':
            print("logout berhasil, terimakasih!\n")
            break
        else:
            print("pilihan tidak valid!\n")
            
  