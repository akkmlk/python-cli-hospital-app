import csv
import datetime as dt
import os
import sys
sys.path.insert(0, 'Controller//Login')
sys.path.insert(0, 'Controller//Admin')
sys.path.insert(0, 'Controller//Increment')
import crud_dokter_fix
import increment

def get_required_input(prompt):
    while True:
        value = input(prompt)
        if value.strip():
            return value
        print("Input tidak boleh kosong. Silakan coba lagi.")

def regist(filename):
    file_exists = os.path.isfile(filename)
    print("Masukkan data untuk membuat akun baru")       
    username = get_required_input("Masukkan username: ")
    password = get_required_input("Masukkan password: ")
    phone = get_required_input("Masukkan Nomor HP: ")
    birth = crud_dokter_fix.validate_date(get_required_input("Masukkan Tanggal Lahir (DD-MM-YYYY): "))

    # users = []

    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file, delimiter=';')
        users = list(reader)
        header = reader.fieldnames
        
        for row in users:
            if username == row['username']:                  
                print("Username sudah ada. Silakan coba lagi.")
                return regist(filename)
            
                    
    # new_id = len(users) + 1 
    # birth = dt.datetime.strftime("%d-%m-%Y")
    akun = {
        'id' : increment.id(users),
        'username': username,
        'password': password,
        'phone_number': phone,
        'date_birth': birth,
        'role': "patient",
    }
    
    with open(filename, mode='a', newline='') as file:
        header = ['id', 'username', 'password', 'phone_number', 'date_birth', 'role']
        writer = csv.DictWriter(file, fieldnames=reader.fieldnames, delimiter=';')

        if not file_exists:
            writer.writeheader ()
        writer.writerow(akun)

    print("Registrasi berhasil!")
    import login
    login.login()