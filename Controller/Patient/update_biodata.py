import csv
import os
from dashboard_patient import *

HEADER = [
    'id', 'name', 'username', 'password', 'phone_number', 'address', 'religion', 'gender', 'place_birth', 'date_birth', 'age_category', 'married', 'last_education', 'blood_type', 'bpjs', 'role', 'doctor_category'
]
# print('apakah anda ingin melengkapi biodata?(ya/tidak): ')
def data_input(prompt):
    while True:
        value = input(prompt)
        if value.strip():
            return value
        print("Input tidak boleh kosong. Silakan coba lagi.")

# def ensure_csv_exists():
#     if not os.path.exists(filename):
#         with open(filename, mode='w', newline='') as file:
#             writer = csv.writer(file, delimiter=';')
#             writer.writerow(HEADER)

# def read_all_data():
#     ensure_csv_exists()
#     with open(filename, mode='r', newline='') as file:
#         reader = csv.DictReader(file, delimiter=';')
#         return list(reader)
    
# def verifikasi(username):
#     data = read_all_data()
#     new_data = [row for row in data if row['username'] != username]
#     if len(new_data) == len(data):
#         print(f"Data dengan username {username} tidak ditemukan.")
#         return
#     else:
#         update(filename, data)

def relation():
    while True:
        married = data_input("Masukkan status pernikahan(Ya/Tidak)")
        if married == "Ya":
            return "Ya"
        elif married == "Tidak":
            return "Tidak"
        else:
            print("Input yang anda masukkan tidak sesuai. Silahkan coba lagi.")

def blood():
    while True:
        blood = data_input("Masukkan golongan darah(A/B/AB/O): ")
        if blood == "A":
            return "A"
        elif blood == "B":
            return "B"
        elif blood == "AB":
            return "AB"
        elif blood == "O":
            return "O"
        else:
            print("Golongan darah tidak valid. Silakan coba lagi.")
        
def input_gender():
    while True:
        gender_input =data_input("Masukkan jenis kelamin (M/W): ").upper()
        if gender_input == 'M':
            return 'Laki-laki'
        elif gender_input == 'W':
            return 'Perempuan'
        else:
            print("Input yang dimasukkan tidak sesuai. ")

def update(filename, patient_data):
    # existing_data = read_all_data()
    print(f"\nId : {patient_data['id']}")
    print(f"Nama : {patient_data['name']}")
    print(f"Username : {patient_data['username']}")
    print(f"Password : {patient_data['password']}")
    print(f"Nomor Handphone : {patient_data['phone_number']}")
    print(f"Alamat : {patient_data['address']}")
    print(f"Agama : {patient_data['religion']}")
    print(f"Jenis Kelamin : {patient_data['gender']}")
    print(f"Tempat Lahir : {patient_data['place_birth']}")
    print(f"Tanggal Lahir : {patient_data['date_birth']}")
    print(f"Sudah Nikah? : {patient_data['married']}")
    print(f"Pendidikan Terakhir : {patient_data['last_education']}")
    print(f"Golongan Darah : {patient_data['blood_type']}")
    print(f"BPJS : {patient_data['bpjs']}")
    print(f"Peran : {patient_data['role']}\n")

    data = {}
    print("masukkan data untuk melengkapi biodata")
    data['name'] = data_input("Masukkan nama lengkap: ")
    data['address'] = data_input("Masukkan alamat saat ini: ")
    data['religion'] = data_input("Masukkan agama: ")
    data['gender'] = input_gender() 
    data['place_birth'] = data_input("Masukkan tempat lahir: ")
    # data['birth_date'] = data_input("Masukkan tanggal lahir: ")
    data['married'] = relation()
    data['last_education'] = data_input("Masukkan pendidikan terakhir: ")
    data['blood_type'] = blood()
    data['bpjs'] = input("Masukkan nomor BPJS: ")  


    for row in existing_data:
        # if row(max['id']) in ['id']:
        row['name'] = data['name']
        row['address'] = data['address']
        row['religion'] = data['religion']
        row['gender'] = data['gender']
        row['place_birth'] = data['place_birth']
        row['age_category'] = data['age_category']
        row['last_education'] = data['last_education']
        row['blood_type'] = data['blood_type']
        row['bpjs'] = data['bpjs']
        row['doctor_category'] = ''
        break

    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=HEADER, delimiter=';')
        writer.writeheader()
        writer.writerows(existing_data)
os.system("cls")




