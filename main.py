

nilai_siswa = [['Jaemin', 80], ['Mark', 90], ['Jeno', 85], ['Renjun', 88], ['Haechan', 92]]

def display_menu():
    print("== DATA NILAI SISWA ==")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Hitung rata-rata")
    print("4. Keluar")
    
def tambah_data():
    nama = input("Masukkan nama siswa: ")
    nilai = int(input("Masukkan nilai siswa: "))
    
    if nilai >= 0 and nilai <= 100:
        nilai_siswa.append([nama, nilai])
        print("Data berhasil ditambahkan!")
    else:
        print("Nilai harus antara 0-100!")
    
def tampilkan_data():
    print("Data Nilai Siswa:")
    for siswa in nilai_siswa:
        print(f"{siswa[0]}: {siswa[1]}")
        
def hitung_rata_rata():
    total_nilai = sum(siswa[1] for siswa in nilai_siswa)
    rata_rata = total_nilai / len(nilai_siswa)
    print(f"Rata-rata nilai siswa: {rata_rata:.2f}")
    
while True:
    display_menu()
    pilihan = input("Pilih menu (1-4): ")
    
    if pilihan == '1':
        tambah_data()
    elif pilihan == '2':
        tampilkan_data()
    elif pilihan == '3':
        hitung_rata_rata()
    elif pilihan == '4':
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")