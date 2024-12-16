import csv
import os
from datetime import datetime

FILE_NAME = 'Database/user.csv'
HEADER = [
    'id;name;username;password;phone_number;address;religion;gender;place_birth;date_birth;age_category;married;last_education;blood_type;bpjs;role;doctor_category'
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
    value = input(prompt)
    while value == '':
        print("Input tidak boleh kosong. Silakan coba lagi.")
        value = input(prompt)
    return value

def validate_date(date_str):
    date_obj = datetime.strptime(date_str, "%d-%m-%Y")
    return date_obj.strftime("%d-%m-%Y")

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
    data['date_birth'] = validate_date(get_required_input("Masukkan tanggal lahir (dd-mm-yyyy): "))
    data['age_category'] = get_required_input("Masukkan kategori usia: ")
    data['married'] = get_required_input("Masukkan status pernikahan: ")
    data['last_education'] = get_required_input("Masukkan pendidikan terakhir: ")
    data['blood_type'] = get_required_input("Masukkan golongan darah: ")
    data['bpjs'] = get_required_input("Masukkan nomor BPJS: ")
    return data

def collect_update_input():
    updated_data = {}
    updated_data['name'] = input("Masukkan nama baru (kosongkan jika tidak ingin mengubah): ")
    updated_data['username'] = input("Masukkan username baru (kosongkan jika tidak ingin mengubah): ")
    updated_data['password'] = input("Masukkan password baru (kosongkan jika tidak ingin mengubah): ")
    updated_data['phone_number'] = input("Masukkan nomor telepon baru (kosongkan jika tidak ingin mengubah): ")
    updated_data['address'] = input("Masukkan alamat baru (kosongkan jika tidak ingin mengubah): ")
    updated_data['religion'] = input("Masukkan agama baru (kosongkan jika tidak ingin mengubah): ")
    updated_data['gender'] = input("Masukkan jenis kelamin baru (kosongkan jika tidak ingin mengubah): ")
    updated_data['place_birth'] = input("Masukkan tempat lahir baru (kosongkan jika tidak ingin mengubah): ")
    updated_data['date_birth'] = input("Masukkan tanggal lahir baru (dd-mm-yyyy, kosongkan jika tidak ingin mengubah): ")
    if updated_data['date_birth'] != '':
        updated_data['date_birth'] = validate_date(updated_data['date_birth'])
    updated_data['age_category'] = input("Masukkan kategori usia baru (kosongkan jika tidak ingin mengubah): ")
    updated_data['married'] = input("Masukkan status pernikahan baru (kosongkan jika tidak ingin mengubah): ")
    updated_data['last_education'] = input("Masukkan pendidikan terakhir baru (kosongkan jika tidak ingin mengubah): ")
    updated_data['blood_type'] = input("Masukkan golongan darah baru (kosongkan jika tidak ingin mengubah): ")
    updated_data['bpjs'] = input("Masukkan nomor BPJS baru (kosongkan jika tidak ingin mengubah): ")
    updated_data['role'] = input("Masukkan peran baru (kosongkan jika tidak ingin mengubah): ")
    return {k: v for k, v in updated_data.items() if v != ''}

def create_receptionist(data):
    ensure_csv_exists()
    data['id'] = str(get_next_id())
    data['role'] = 'Resepsionis'
    if data['date_birth'] != '':
        data['date_birth'] = validate_date(data['date_birth'])
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=HEADER[0].split(';'), delimiter=';')
        writer.writerow(data)
    print("Data berhasil ditambahkan.")


def read_receptionist():
    data = read_all_data()
    receptionist_data = [row for row in data if row['role'] == 'resepsionis']
    if len(receptionist_data) == 0:
        print("Tidak ada data resepsionis.")
        return
    print("\n" + "="*171)
    print(f"{'ID':<5}{'|':<2}{'Nama':<20}{'|':<2}{'Alamat':<20}{'|':<2}{'Agama':<10}{'|':<2}{'Gender':<15}{'|':<2}{'Tanggal Lahir':<15}{'|':<2}{'Usia':<15}{'|':<2}{'Gol Darah':<10}{'|':<2}{'BPJS':<10}{'|':<2}{'Peran':<10}|")
    print("-"*171)
    for row in receptionist_data:
        print(f"{row['id']:<5}{'|':<2}{row['name']:<20}{'|':<2}{row['address']:<20}{'|':<2}{row['religion']:<10}{'|':<2}{row['gender']:<15}{'|':<2}{row['date_birth']:<15}{'|':<2}{row['age_category']:<15}{'|':<2}{row['blood_type']:<10}{'|':<2}{row['bpjs']:<10}{'|':<2}{row['role']:<10}|")
    print("="*171)

def update_receptionist():
    data = read_all_data()
    receptionist_id = get_required_input("Masukkan ID resepsionis yang akan diperbarui: ")
    found = False
    for row in data:
        if row['id'] == str(receptionist_id):
            found = True
            print(f"Data ditemukan untuk ID {receptionist_id}. Lanjutkan dengan memperbarui.")
            updated_data = collect_update_input()
            for key, value in updated_data.items():
                if key == 'date_birth' and value != '':
                    value = validate_date(value)
                row[key] = value
            break
    if not found:
        print(f"Data dengan ID {receptionist_id} tidak ditemukan.")
        return
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=HEADER[0].split(';'), delimiter=';')
        writer.writeheader()
        writer.writerows(data)
    print("Data berhasil diperbarui.")

def delete_receptionist(receptionist_id):
    data = read_all_data()
    new_data = [row for row in data if row['id'] != str(receptionist_id)]
    if len(new_data) == len(data):
        print(f"Data dengan ID {receptionist_id} tidak ditemukan.")
        return
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=HEADER[0].split(';'), delimiter=';')
        writer.writeheader()
        writer.writerows(new_data)
    print("Data berhasil dihapus.")

def main_resepsionis():
    ensure_csv_exists()
    while True:
        print("\nMenu:")
        print("1. Tambah resepsionis")
        print("2. Lihat data resepsionis")
        print("3. Perbarui data resepsionis")
        print("4. Hapus data resepsionis")
        print("5. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            data_receptionist = collect_receptionist_input()
            create_receptionist(data_receptionist)
        elif pilihan == '2':
            read_receptionist()
        elif pilihan == '3':
            update_receptionist
        elif pilihan == '4':
            doctor_id = input("Masukkan ID dokter yang akan dihapus: ")
            delete_receptionist(doctor_id)
        elif pilihan == '5':
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")