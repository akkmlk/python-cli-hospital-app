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


    print("\n" + "="*171)
    print(f"{'ID':<5}{'|':<2}{'Nama':<20}{'|':<2}{'Alamat':<20}{'|':<2}{'Agama':<10}{'|':<2}{'Gender':<15}{'|':<2}{'Tanggal Lahir':<15}{'|':<2}{'Usia':<15}{'|':<2}{'Gol Darah':<10}{'|':<2}{'BPJS':<10}{'|':<2}{'Peran':<10}{'|':<2}{'Kategori':<20}|")
    print("-"*171)
    for row in data:
        print(f"{row['id']:<5}{'|':<2}{row['name']:<20}{'|':<2}{row['address']:<20}{'|':<2}{row['religion']:<10}{'|':<2}{row['gender']:<15}{'|':<2}{row['date_birth']:<15}{'|':<2}{row['age_category']:<15}{'|':<2}{row['blood_type']:<10}{'|':<2}{row['bpjs']:<10}{'|':<2}{row['role']:<10}{'|':<2}{row['category']:<20}|")
    print("="*171)


def update_receptionist(receptionist_id, updated_data):
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

        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            data = collect_receptionist_input()
            create_receptionist(data)

        elif pilihan == '2':
            read_receptionists()  

        elif pilihan == '3':
            receptionist_id = input("Masukkan ID resepsionis yang ingin diperbarui: ")
            updated_data = collect_receptionist_input()
            update_receptionist(receptionist_id, updated_data)

        elif pilihan == '4':
            receptionist_id = input("Masukkan ID resepsionis yang ingin dihapus: ")
            delete_receptionist(receptionist_id)

        elif pilihan == '5':
            print("Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
