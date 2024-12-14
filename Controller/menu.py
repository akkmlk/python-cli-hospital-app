def menu():
    # Tentukan path file CSV di sini
    path = r"D:\KULIAH\SEMESTER 1\I. ALGORITHM & FUNDAMENTALS OF PRACTICAL PROGRAMMING\ASSIGNMENT\python-cli-hospital-app\Database\user.csv"
    
    
    
    while True:
        print("\nMenu CRUD Dokter:")
        print("1. Tambah Dokter")
        print("2. Lihat Dokter")
        print("3. Update Dokter")
        print("4. Hapus Dokter")
        print("5. Keluar")
        
        pilihan = input("Pilih opsi: ")
        
        if pilihan == '1':
            name = input("Masukkan nama dokter: ")
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")
            phone_number = input("Masukkan nomor telepon dokter: ")
            address = input("Masukkan alamat dokter: ")
            religion = input("Masukkan agama dokter: ")
            gender = input("Masukkan jenis kelamin dokter: ")
            place_birth = input("Masukkan tempat lahir dokter: ")
            date_birth = input("Masukkan tanggal lahir dokter: ")
            age_category = input("Masukkan kategori usia dokter: ")
            married = input("Masukkan status pernikahan dokter: ")
            last_education = input("Masukkan pendidikan terakhir dokter: ")
            blood_type = input("Masukkan golongan darah dokter: ")
            bpjs = input("Masukkan status BPJS dokter: ")
            role = input("Masukkan peran dokter: ")
            doctor_category = input("Masukkan kategori dokter: ")
            add_dokter(path, name, username, password, phone_number, address, religion, gender, place_birth, date_birth, age_category, married, last_education, blood_type, bpjs, role, doctor_category)
        
        elif pilihan == '2':
            print("\nDaftar Dokter:")
            read_dokter(path)
        
        elif pilihan == '3':
            id = input("Masukkan ID dokter yang ingin diperbarui: ")
            name = input("Masukkan nama baru (biarkan kosong untuk tidak mengubah): ")
            username = input("Masukkan username baru (biarkan kosong untuk tidak mengubah): ")
            password = input("Masukkan password baru (biarkan kosong untuk tidak mengubah): ")
            phone_number = input("Masukkan nomor telepon baru (biarkan kosong untuk tidak mengubah): ")
            address = input("Masukkan alamat baru (biarkan kosong untuk tidak mengubah): ")
            religion = input("Masukkan agama baru (biarkan kosong untuk tidak mengubah): ")
            gender = input("Masukkan jenis kelamin baru (biarkan kosong untuk tidak mengubah): ")
            place_birth = input("Masukkan tempat lahir baru (biarkan kosong untuk tidak mengubah): ")
            date_birth = input("Masukkan tanggal lahir baru (biarkan kosong untuk tidak mengubah): ")
            age_category = input("Masukkan kategori usia baru (biarkan kosong untuk tidak mengubah): ")
            married = input("Masukkan status pernikahan baru (biarkan kosong untuk tidak mengubah): ")
            last_education = input("Masukkan pendidikan terakhir baru (biarkan kosong untuk tidak mengubah): ")
            blood_type = input("Masukkan golongan darah baru (biarkan kosong untuk tidak mengubah): ")
            bpjs = input("Masukkan status BPJS baru (biarkan kosong untuk tidak mengubah): ")
            role = input("Masukkan peran baru (biarkan kosong untuk tidak mengubah): ")
            doctor_category = input("Masukkan kategori dokter baru (biarkan kosong untuk tidak mengubah): ")
            update_dokter(path, id, name, username, password, phone_number, address, religion, gender, place_birth, date_birth, age_category, married, last_education, blood_type, bpjs, role, doctor_category)
        
        elif pilihan == '4':
            id = input("Masukkan ID dokter yang ingin dihapus: ")
            delete_dokter(path, id)
        
        elif pilihan == '5':
            print("Keluar dari program.")
            break
        
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

# Menjalankan program
menu()
