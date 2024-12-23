import csv
import os
import dashboard_patient

HEADER = [
    'id', 'name', 'username', 'password', 'phone_number', 'address', 'religion', 'gender', 'place_birth', 'date_birth', 'age_category', 'married', 'last_education', 'blood_type', 'bpjs', 'role', 'doctor_category'
]

def data_input(prompt):
    while True:
        value = input(prompt)
        if value.strip():
            return value
        print("Input tidak boleh kosong. Silakan coba lagi.")

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
    print(f"Pendidikan Terakhir : {patient_data['last_education']}")
    print(f"Golongan Darah : {patient_data['blood_type']}")
    print(f"BPJS : {patient_data['bpjs']}")
    print(f"Peran : {patient_data['role']}\n")

    print("masukkan data untuk melengkapi biodata")
    data = {}
    data['name'] = data_input("Masukkan nama lengkap: ")
    data['address'] = data_input("Masukkan alamat saat ini: ")
    data['religion'] = data_input("Masukkan agama: ")
    data['gender'] = input_gender() 
    data['place_birth'] = data_input("Masukkan tempat lahir: ")
    data['last_education'] = data_input("Masukkan pendidikan terakhir: ")
    data['blood_type'] = blood()
    data['bpjs'] = input("Masukkan nomor BPJS: ")  

    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file, delimiter=';')
        existing_data = list(reader)
        header = reader.fieldnames

    for row in existing_data:
        if row['id'] == patient_data['id']:
            row['name'] = data['name']
            row['address'] = data['address']
            row['religion'] = data['religion']
            row['gender'] = data['gender']
            row['place_birth'] = data['place_birth']
            row['last_education'] = data['last_education']
            row['blood_type'] = data['blood_type']
            row['bpjs'] = data['bpjs']
            row['doctor_category'] = ''
            break

    with open(filename, mode='w', newline='') as write:
        writer = csv.DictWriter(write, fieldnames=header, delimiter=';')
        writer.writeheader()
        writer.writerows(existing_data)
    
    print("Data Updated")
    os.system("cls")
    dashboard_patient.menu_patient(patient_data)