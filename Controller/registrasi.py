import csv
import datetime as dt
import os

def get_required_input(prompt):
    while True:
        value = input(prompt)
        if value.strip():
            return value
        print("Input tidak boleh kosong. Silakan coba lagi.")

print("Masukkan data untuk membuat akun baru")       
username = get_required_input("Masukkan username: ")
password = get_required_input("Masukkan password: ")
phone = get_required_input("Masukkan Nomor HP: ")
birth = get_required_input("Masukkan Tanggal Lahir (DD-MM-YYYY): ")

def regist(filename):

    file_exists = os.path.isfile(filename)
    
    users = []
      
    
    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file, delimiter=';')
        users = list(reader)
        for row in users:
            if username == row['username']:
                print("Username sudah ada. Silakan coba lagi.")
                return

    new_id = len(users) + 1 

    akun = {
        'id' : new_id,
        'username': username,
        'password': password,
        'phone_number': phone,
        'date_birth': birth,
        'role' : 'patient'
    }
    with open(filename, mode='a', newline='') as file:
        header = ['id', 'username', 'password', 'phone_number', 'date_birth','role']
        writer = csv.DictWriter(file, fieldnames=reader.fieldnames, delimiter=';')

        if not file_exists:
            writer.writeheader ()
        writer.writerow(akun)

    print("Registrasi berhasil!")
    print("Anda telah membuat akun baru")
    print("ID Anda: ", new_id)

regist('Database/user.csv')


      


