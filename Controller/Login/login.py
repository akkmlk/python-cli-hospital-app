import csv
import os
import datetime as dt
import sys
sys.path.insert(0, 'C://tugas ngoding//python-cli-hospital-app//Controller//Patient')
sys.path.insert(0, 'C://tugas ngoding//python-cli-hospital-app//Controller//Doctor')
sys.path.insert(0, 'C://tugas ngoding//python-cli-hospital-app//Controller//Admin')
sys.path.insert(0, 'C://tugas ngoding//python-cli-hospital-app//Controller//Receptionis')
sys.path.insert(0, 'C://tugas ngoding//python-cli-hospital-app//Controller//Register')
import dashboard_patient
import dashboard_doctor
import dashboard_admin
import dashboard_receptionis
import registration

otp = 'password'

def question_have_account():
    print("Selamat Datang")
    while True:
        haved_account = input("Apakah kamu sudah punya akun? (Y/N) : ").lower()
        if haved_account != "":
            if haved_account == "y":
                login()
                return False
            elif haved_account == "n":
                registration.regist('Database/user.csv')
                return False
            else:
                print("Silahkan pilih Y/N")
        else:
            print("Silahkan pilih Y/N")

# temporary_log = []

def login ():
    os.system('cls')
    print("Silahkan login")
    trial = 0
    filelog = 'Database/log.csv'

    while trial < 3:
        username = str(input("Masukan Username: "))
        password = str(input("Masukan Password: "))
        
        
        with open('Database/user.csv', mode='r') as file:
            reader = csv.DictReader(file, delimiter= ';')

            data = list(reader)

            detect_user = False
            for row in data:
                if username == row['username'] and password == row[otp]:

                    if row['role'] == 'doctor':
                        detect_user = True
                        log_csv(filelog, username, password, "Berhasil")
                        patient_data = temporary_login(row['id'], row['name'], row['username'], row['password'], row['phone_number'], row['address'], row['religion'], row['gender'], row['place_birth'], row['date_birth'], row['last_education'], row['blood_type'], row['bpjs'], row['role'], row['doctor_category'])
                        print("login dokter berhasil")
                        dashboard_doctor.menu_doctor(patient_data)
                        os.system('pause')
                        # return False

                    elif row['role'] == 'receptionis':
                        detect_user = True
                        temporary_login( row['id'], row['name'], row['username'], row['password'], row['phone_number'], row['address'], row['religion'], row['gender'], row['place_birth'], row['date_birth'], row['last_education'], row['blood_type'], row['bpjs'], row['role'], row['doctor_category'])
                        log_csv(filelog, username, password, "Berhasil") 
                        receptionis_data = temporary_login(row['id'], row['name'], row['username'], row['password'], row['phone_number'], row['address'], row['religion'], row['gender'], row['place_birth'], row['date_birth'], row['last_education'], row['blood_type'], row['bpjs'], row['role'], row['doctor_category'])
                        print("login resepsionis berhasil")
                        dashboard_receptionis.menu_receptionis(receptionis_data)
                        return False                       
                    
                    elif row['role'] == 'admin':
                        detect_user = True
                        temporary_login( row['id'], row['name'], row['username'], row['password'], row['phone_number'], row['address'], row['religion'], row['gender'], row['place_birth'], row['date_birth'], row['last_education'], row['blood_type'], row['bpjs'], row['role'], row['doctor_category'])
                        log_csv(filelog, username, password, "Berhasil")
                        admin_data = temporary_login(row['id'], row['name'], row['username'], row['password'], row['phone_number'], row['address'], row['religion'], row['gender'], row['place_birth'], row['date_birth'], row['last_education'], row['blood_type'], row['bpjs'], row['role'], row['doctor_category'])
                        print("login admin berhasil")
                        dashboard_admin.menu_admin(admin_data)
                        return False
                    elif row['role'] == 'patient':
                        patient_data = temporary_login( row['id'], row['name'], row['username'], row['password'], row['phone_number'], row['address'], row['religion'], row['gender'], row['place_birth'], row['date_birth'], row['last_education'], row['blood_type'], row['bpjs'], row['role'], row['doctor_category'])
                        detect_user = True
                        log_csv(filelog, username, password, "Berhasil")
                        print("login pasien berhasil")
                        dashboard_patient.menu_patient(patient_data)
                        return False
                    else:
                        detect_user = False
                        log_csv(filelog, username, password, "Gagal")
                        print("Login gagal")
                        return False

            if detect_user == False:
                print("Login Gagal")
                log_csv(filelog, username, password, "Gagal")
                trial += 1
                os.system('pause')
            
    os.system('break')    

def log_csv(filename, username, password, status):
    detect_log = os.path.isfile(filename)
    
    data = [
        {
            'Timestamp' : dt.datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            'Username' : username,
            'Password' : password,
            'Status' : status
        }
    ]

    with open(filename, mode='a', newline='') as file: 
            header = ['Timestamp', 'Username', 'Password', 'Status']

            writer = csv.DictWriter(file, fieldnames=header)

            if not detect_log:
                writer.writeheader()
            
            writer.writerows(data)

def temporary_login(id, name, username, password,phone_number,address,religion,gender,place_birth,date_birth,last_education,blood_type,bpjs,role,doctor_category):
    patient_data = {
        'id' : id,
        'name' : name,
        'username' : username,
        'password' : password,
        'phone_number' : phone_number,
        'address' : address,
        'religion' : religion,
        'gender' : gender,
        'place_birth' : place_birth,
        'date_birth' : date_birth,
        'last_education' : last_education,
        'blood_type' : blood_type,
        'bpjs' : bpjs,
        'role' : role,
        'doctor_category' : doctor_category
    }
    return patient_data

question_have_account()
