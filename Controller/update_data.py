import csv
import os

filename = 'Database/user.csv'
HEADER = [
    'id', 'name', 'username', 'password', 'phone_number', 'address', 'religion', 'gender', 'place_birth', 'date_birth', 'age_category', 'married', 'last_education', 'blood_type', 'bpjs', 'role', 'doctor_category'
]
# print('apakah anda ingin melengkapi biodata?(ya/tidak): ')
def Data_input(prompt):
    while True:
        value = input(prompt)
        if value.strip():
            return value
        print("Input tidak boleh kosong. Silakan coba lagi.")

def ensure_csv_exists():
    if not os.path.exists(filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(HEADER)

def read_all_data():
    ensure_csv_exists()
    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file, delimiter=';')
        return list(reader)
    

def verifikasi(username):
    data = read_all_data()
    new_data = [row for row in data if row['username'] != username]
    if len(new_data) == len(data):
        print(f"Data dengan username {username} tidak ditemukan.")
        return
    else:
        update(filename, data)
    
# print("masukkan data akun yang ingin diupdate")
# username = Data_input("Masukkan username: ")
# password = Data_input("Masukkan password: ")
# phone = Data_input("Masukkan Nomor HP: ")
# birth = Data_input("Masukkan Tanggal Lahir (DD-MM-YYYY): ")

data = {}   

def update(filename, data):
    existing_data = read_all_data()
    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file, delimiter=';')
        users = list(reader)
        

    data = {}
    print("masukkan data untuk melengkapi biodata")
    data['name'] = Data_input("Masukkan nama lengkap: ")
    data['address'] = Data_input("Masukkan alamat saat ini: ")
    data['religion'] = Data_input("Masukkan agama: ")
    data['gender'] = Data_input("Masukkan jenis kelamin(M/W): ")
    if data['gender'] == 'M':
        data['gender'] = 'Laki-laki'
    else:
        data['gender'] = 'Perempuan'
    data['place_birth'] = Data_input("Masukkan tempat lahir: ")
    # data['birth_date'] = Data_input("Masukkan tanggal lahir: ")
    data['age_category'] = Data_input("Masukkan kategori usia(anak-anak/remaja/dewasa): ")
    data['married'] = Data_input("Masukkan status pernikahan(Ya/Tidak): ")
    data['last_education'] = Data_input("Masukkan pendidikan terakhir: ")
    data['blood_type'] = Data_input("Masukkan golongan darah: ")
    data['bpjs'] = Data_input("Masukkan nomor BPJS: ")  
     
    
    for row in existing_data:
        # if row(max['id']) in ['id']:
        row['name'] = data['name']
        row['address'] = data['address']
        row['religion'] = data['religion']
        row['gender'] = data['gender']
        
        row['place_birth'] = data['place_birth']
        row['age_category'] = data['age_category']
        row['married'] = data['married']
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

# verifikasi(username)
update(filename, data)



