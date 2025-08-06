# data buku
books = [
    {"isbn":"9786237121144", "judul":"Kumpulan Solusi Pemrograman Python", "pengarang":"Budi Raharjo", "jumlah":6, "terpinjam":0},
    {"isbn":"9786231800718", "judul":"Dasar-Dasar Pengembangan Perangkat Lunak dan Gim Vol. 2", "pengarang":"Okta Purnawirawan", "jumlah":15, "terpinjam":0},
    {"isbn":"9786026163905", "judul":"Analisis dan Perancangan Sistem Informasi", "pengarang":"Adi Sulistyo Nugroho", "jumlah":2, "terpinjam":1},
    {"isbn":"9786022912828", "judul":"Animal Farm", "pengarang":"George Orwell", "jumlah":4, "terpinjam":0},
]
# data peminjaman
records = [
    {"isbn":"9786022912828", "status":"Selesai", "tanggal_pinjam":"2025-03-21", "tanggal_kembali":"2025-03-28"},
    {"isbn":"9786026163905", "status":"Belum", "tanggal_pinjam":"2025-07-22", "tanggal_kembali":""},
]

def bersih(): 
    import time 
    import os 
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_data():
    print("===== Menu tampilkan data buku =====")
    print("")
    for i in range(len(books)):
        print(i+1, "\t", end=" ")
        print(books[i] [f"isbn"], "\t", books[i] [f"judul"], "\t", books[i] [f"pengarang"], "\t", books[i] [f"jumlah"], "\t", books[i] [f"terpinjam"], "\t",)
    
    print("==================================================================================================================================================================================")

def tambah_data():
    print("===== Menu tambah buku =====")
    isbn = int(input("Masukkan isbn buku yang ingin ditambahkan :"))
    judul = str(input("Masukkan judul buku yang ada :"))
    pengarang = str(input("Masukkan nama pengarang :"))
    jumlah = int(input("Masukkan jumlah buku yang tersedia :"))
    terpinjam = int(input("Masukkan buku yang telah dipinjam :"))
    buku6 = {"isbn":isbn, "judul" : judul, "pengarang" : pengarang, "jumlah" : jumlah, "terpinjam" : terpinjam}
    books.append(buku6)
    print("==================================================================================================================================================================================")

def edit_data():
    print("===== Menu edit buku =====")
    tampilkan_data()
    index = int(input("Pilih buku yang ingin diubah : ")) - 1

    books[index]["isbn"] = int(input("Masukkan isbn buku baru : "))
    books[index]["judul"] = str(input("Masukkan judul baru : "))
    books[index]["pengarang"] = str(input("Masukkan pengarang baru : "))
    books[index]["jumlah"] = int(input("Masukkan jumlah baru : "))
    books[index]["terpinjam"] = int(input("Masukkan terpinjam baru : "))
    print("Data berhasil di edit")
    print("==================================================================================================================================================================================")

def hapus_data():
    print("===== Menu hapus buku =====")
    tampilkan_data()
    for i in range(len(books)):
        print(i+1, "\t", end=" ")
        print(books[i] ["isbn"], "\t", books[i] ["judul"], "\t", books[i] ["pengarang"], "\t", books[i] ["jumlah"], "\t", books[i] ["terpinjam"], "\t",)

    mana = int(input("Pilih buku yang ingin dihapus")) - 1
    if mana >= 0 and mana < len(books):
        del books[mana - 1]
        print("Buku berhasil dihapus")

    else:
        print("Tidak buku yang bisa dihapus")
    print("==================================================================================================================================================================================")

def tampilkan_peminjaman():
    print("===== Menu tampilkan buku yang dipinjam =====")
    for i in range(len(records)):
        print(i+1, "\t", end=" ")
        print(records[i] ["isbn"], "\t", records[i] ["status"], "\t", records[i] ["tanggal_pinjam"], "\t", records[i] ["tanggal_kembali"], "\t")
    print("==================================================================================================================================================================================")

def tampilkan_belum():
    print("===== Menu tampilkan buku yang dipinjam namun belum kembali =====")
    j = 1
    for i in range(len(records)):
        if records[i]["status"] == "Belum":
                print(j, "\t", end=" ")
                print(records[i]["isbn"], "\t", records[i]["status"], "\t", records[i]["tanggal_pinjam"], "\t", records[i]["tanggal_kembali"], "\t")
                j += 1
            
        else:
            print("Semua buku sudah dikembalikan")
    print("==================================================================================================================================================================================")

def peminjaman():
    print("===== Menu pinjam buku =====")
    isbn = int(input("Masukkan isbn buku yang ingin ditambahkan : "))
    status = str(input("Masukkan status buku yang ada : "))
    tanggal_pinjam = str(input("Masukkan tanggal pinjam : "))
    tanggal_kembali = str(input("Masukkan tanggal kembali : "))
    peminjam = {"isbn":isbn, "status" : status, "tanggal_pinjam" : tanggal_pinjam, "tanggal_kembali" : tanggal_kembali}
    records.append(peminjam)
    print("==================================================================================================================================================================================")

def pengembalian():
    print("===== Menu pengembalian buku =====")
    tampilkan_peminjaman()

    index = int(input("Pilih buku yang ingin dikembalikan : ")) - 1

    records[index]["status"] = "Selesai"
    records[index]["tanggal_kembali"] = str(input("Masukkan tanggal kembali : "))
    print("==================================================================================================================================================================================")


while True:
    print("---=== MENU ===---")
    print("[1] Tampilkan Data")
    print("[2] Tambah Data")
    print("[3] Edit Data")
    print("[4] Hapus Data")
    print("------------------")
    print("[5] Tampilkan Semua Peminjaman")
    print("[6] Tampilkan Peminjaman Belum Kembali")
    print("[7] Peminjaman")
    print("[8] Pengembalian")
    print("[X] Keluar")

    menu = input("Masukkan pilihan menu (1-8 atau x): ")
    bersih()
    
    if menu == "1":
        tampilkan_data()

    elif menu == "2":
        tambah_data()

    elif menu == "3":
        edit_data()

    elif menu == "4":
        hapus_data()

    elif menu == "5":
        tampilkan_peminjaman()

    elif menu == "6":
        tampilkan_belum()

    elif menu == "7":
        peminjaman()

    elif menu == "8":
        pengembalian()

    elif menu.lower() == "x":
        print("Terima kasih telah menggunakan program ini.")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")