print("halooo!")
usn = input("Buat dulu username anda: ")
pw = input("Buat dulu password anda: ")
salah = 0

while salah < 3:
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    if username == usn and password == pw :
        print("selamat datang sayanggku")
        break
    else:
        print("yahh gagal login WKWKWK")
        salah += 1
        if salah == 3: 
            print("kamu sudah coba 3 kali lohh, aku blokir yaa maaf")
            exit( )

while True :
            Nama = input("Masukkan Nama: ")
            NIM = input ("Masukkan NIM: ")
            jumlah_pinjaman = float(input("Masukkan Jumlah Pinjaman: "))

            print("\nPilih Lama Cicilan: ")
            print("1. 1 tahun")
            print("2. 2 tahun")
            print("3. 3 tahun")

            lama_cicilan = int(input("Masukkan Pilihan Lama Cicilan (1,2, atau 3): "))

            if lama_cicilan == 1 :
                 bunga_tahunan = 0.07
                 jumlah_bulan = 12
            elif lama_cicilan == 2 :
                 bunga_tahunan = 0.13
                 jumlah_bulan = 24
            elif lama_cicilan == 3 :
                 bunga_tahunan = 0.19
                 jumlah_bulan = 36
            else:
                print("Pilihan tidak valid!!!")
                exit ( )


            bunga_per_bulan = (bunga_tahunan / 12) * jumlah_pinjaman

            total_cicilan_per_bulan = (jumlah_pinjaman + bunga_per_bulan) / jumlah_bulan

            print(f"\nNama: {Nama}")
            print(f"NIM: {NIM}")
            print(f"Jumlah Pinjaman: Rp{jumlah_pinjaman}")
            print(f"Lama Cicilan: {jumlah_bulan} Bulan")
            print(f"Total Cicilan Per Bulan: Rp{total_cicilan_per_bulan: 2f}")

            ulangi= input("apakah anda ingin menghitung lagi? ketik 'yap' untuk melanjutkan, atau 'nah' untuk keluar: ")
            if ulangi == "nah" :
                print("yeyyy program selesai, terima kasih dan semangat sayang!")
                break 