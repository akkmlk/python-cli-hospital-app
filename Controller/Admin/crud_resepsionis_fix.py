import csv
import os
from datetime import datetime

FILE_NAME = 'Database/user.csv'
HEADER = [
    'id;name;username;password;phone_number;address;religion;gender;place_birth;date_birth;age_category;married;last_education;blood_type;bpjs;role;category'
]

def ensure_csv_exists():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(HEADER[0].split(';'))

def read_all_data():
    ensure_csv_exists()
    with open(FILE_NAME, mode='r') as file:
        reader = csv.DictReader(file, delimiter=';')
        return list(reader)

def get_next_id():
    data = read_all_data()
    valid_ids = [int(row['id']) for row in data if row['id'].isdigit()]
    return max(valid_ids, default=0) + 1

def get_required_input(prompt):
    while True:
        value = input(prompt)
        if value.strip():
            return value
        print("Input tidak boleh kosong. Silakan coba lagi.")

def get_valid_date(prompt):
    while True:
        date_input = input(prompt)
        try:
            datetime.strptime(date_input, "%d-%m-%Y")
            return date_input
        except ValueError:
            print("Format tanggal salah. Harus dalam format dd-mm-yyyy. Silakan coba lagi.")

def collect_receptionist_input():
    data = {}
    data['name'] = get_required_input("Masukkan nama: ")
    data['username'] = get_required_input("Masukkan username: ")
    data['password'] = get_required_input("Masukkan password: ")
    data['phone_number'] = get_required_input("Masukkan nomor telepon: ")
    data['address'] = get_required_input("Masukkan alamat: ")
    data['religion'] = get_required_input("Masukkan agama: ")
    data['gender'] = get_required_input("Masukkan jenis kelamin: ")
    data['place_birth'] = get_required_input("Masukkan tempat lahir: ")
    data['date_birth'] = get_valid_date("Masukkan tanggal lahir (dd-mm-yyyy): ")
    data['age_category'] = get_required_input("Masukkan kategori usia: ")
    data['married'] = get_required_input("Masukkan status pernikahan: ")
    data['last_education'] = get_required_input("Masukkan pendidikan terakhir: ")
    data['blood_type'] = get_required_input("Masukkan golongan darah: ")
    data['bpjs'] = get_required_input("Masukkan nomor BPJS: ")
    data['category'] = ''  
    return data

def collect_optional_input():
    print("Tekan Enter jika tidak ingin mengubah data tersebut.")
    data = {}
    data['name'] = input("Masukkan nama (kosongkan jika tidak ingin mengubah): ")
    data['username'] = input("Masukkan username (kosongkan jika tidak ingin mengubah): ")
    data['password'] = input("Masukkan password (kosongkan jika tidak ingin mengubah): ")
    data['phone_number'] = input("Masukkan nomor telepon (kosongkan jika tidak ingin mengubah): ")
    data['address'] = input("Masukkan alamat (kosongkan jika tidak ingin mengubah): ")
    data['religion'] = input("Masukkan agama (kosongkan jika tidak ingin mengubah): ")
    data['gender'] = input("Masukkan jenis kelamin (kosongkan jika tidak ingin mengubah): ")
    data['place_birth'] = input("Masukkan tempat lahir (kosongkan jika tidak ingin mengubah): ")
    
    while True:
        date_input = input("Masukkan tanggal lahir (dd-mm-yyyy) (kosongkan jika tidak ingin mengubah): ")
        if not date_input.strip():
            break  # Jika kosong, lanjut tanpa perubahan
        try:
            datetime.strptime(date_input, "%d-%m-%Y")
            data['date_birth'] = date_input
            break
        except ValueError:
            print("Format tanggal salah. Harus dalam format dd-mm-yyyy. Silakan coba lagi.")
    
    data['age_category'] = input("Masukkan kategori usia (kosongkan jika tidak ingin mengubah): ")
    data['married'] = input("Masukkan status pernikahan (kosongkan jika tidak ingin mengubah): ")
    data['last_education'] = input("Masukkan pendidikan terakhir (kosongkan jika tidak ingin mengubah): ")
    data['blood_type'] = input("Masukkan golongan darah (kosongkan jika tidak ingin mengubah): ")
    data['bpjs'] = input("Masukkan nomor BPJS (kosongkan jika tidak ingin mengubah): ")
    return {key: value for key, value in data.items() if value.strip()}

def create_receptionist(data):
    ensure_csv_exists()
    data['id'] = str(get_next_id())
    data['role'] = 'Resepsionis' 
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=HEADER[0].split(';'), delimiter=';')
        writer.writerow(data)
    print("Data resepsionis berhasil ditambahkan.")

def read_receptionists():
    data = [row for row in read_all_data() if row['role'] == 'Resepsionis']
    if not data:
        print("Tidak ada data resepsionis.")
        return

    print("\n+" + "="*151)
    print(f"{'ID':<5}{'|':<2}{'Nama':<20}{'|':<2}{'Alamat':<20}{'|':<2}{'Agama':<10}{'|':<2}{'Gender':<15}{'|':<2}{'Tanggal Lahir':<15}{'|':<2}{'Usia':<15}{'|':<2}{'Gol Darah':<10}{'|':<2}{'BPJS':<10}{'|':<2}{'Peran':<12}|")
    print("-"*151)
    for row in data:
        print(f"{row['id']:<5}{'|':<2}{row['name']:<20}{'|':<2}{row['address']:<20}{'|':<2}{row['religion']:<10}{'|':<2}{row['gender']:<15}{'|':<2}{row['date_birth']:<15}{'|':<2}{row['age_category']:<15}{'|':<2}{row['blood_type']:<10}{'|':<2}{row['bpjs']:<10}{'|':<2}{row['role']:<10}1|")
    print("="*151)

def update_receptionist(receptionist_id, updated_data):
    if not receptionist_id.strip():
        print("ID wajib diisi untuk memperbarui data.")
        return

    data = read_all_data()
    found = False
    for row in data:
        if row['id'] == str(receptionist_id) and row['role'] == 'Resepsionis':
            found = True
            for key, value in updated_data.items():
                if key == 'date_birth' and value:
                    try:
                        datetime.strptime(value, "%d-%m-%Y")
                        row[key] = value
                    except ValueError:
                        print("Format tanggal salah. Harus dalam format dd-mm-yyyy.")
                        return
                else:
                    row[key] = value
            break
    if not found:
        print(f"Data dengan ID {receptionist_id} tidak ditemukan.")
        return
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=HEADER[0].split(';'), delimiter=';')
        writer.writeheader()
        writer.writerows(data)
    print("Data resepsionis berhasil diperbarui.")

def delete_receptionist(receptionist_id):
    data = read_all_data()
    new_data = [row for row in data if not (row['id'] == str(receptionist_id) and row['role'] == 'Resepsionis')]
    if len(new_data) == len(data):
        print(f"Data dengan ID {receptionist_id} tidak ditemukan.")
        return
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=HEADER[0].split(';'), delimiter=';')
        writer.writeheader()
        writer.writerows(new_data)
    print("Data resepsionis berhasil dihapus.")

if __name__ == '__main__':
    ensure_csv_exists()
    while True:
        print("\nMenu Resepsionis:")
        print("1. Tambah resepsionis")
        print("2. Lihat data resepsionis")
        print("3. Perbarui data resepsionis")
        print("4. Hapus data resepsionis")
        print("5. Keluar")

        option = input("Pilih menu: ")

        if option == '1':
            data = collect_receptionist_input()
            create_receptionist(data)

        elif option == '2':
            read_receptionists()  

        elif option == '3':
            receptionist_id = input("Masukkan ID resepsionis yang ingin diperbarui: ")
            updated_data = collect_optional_input()
            update_receptionist(receptionist_id, updated_data)

        elif option == '4':
            receptionist_id = input("Masukkan ID resepsionis yang ingin dihapus: ")
            delete_receptionist(receptionist_id)

        elif option == '5':
            print("Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
