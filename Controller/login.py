import csv
import os
import datetime as dt
from Patient.dashboard import menu
# sys.path.insert(0, 'D://New-folder//python-cli-hospital-app//Controller//Patient')

otp = 'password'

# temporary_log = []

def login (fileuser, filelog):
    os.system('cls')
    print("Selamat Datang")
    trial = 0

    while trial < 3:
        username = str(input("Masukan Username: "))
        password = str(input("Masukan Password: "))
        
        with open(fileuser, mode='r') as file:
            reader = csv.DictReader(file, delimiter= ';')

            data = list(reader)

            detect_user = False
            for row in data:
                if username == row['username'] and password == row[otp]:

                    if row['role'] == 'doctor':
                        detect_user = True
                        log_csv(filelog, username, password, "Berhasil")
                        temporary( row['id'], row['name'], row['username'], row['password'], row['phone_number'], row['address'], row['religion'], row['gender'], row['place_birth'], row['date_birth'], row['age_category'], row['married'], row['last_education'], row['blood_type'], row['bpjs'], row['role'], row['doctor_category'])
                        print("login dokter berhasil")
                        os.system('pause') # menu_dokter()
                        return False

                    elif row['role'] == 'resepsionis':
                        detect_user = True
                        temporary( row['id'], row['name'], row['username'], row['password'], row['phone_number'], row['address'], row['religion'], row['gender'], row['place_birth'], row['date_birth'], row['age_category'], row['married'], row['last_education'], row['blood_type'], row['bpjs'], row['role'], row['doctor_category'])
                        log_csv(filelog, username, password, "Berhasil")                        
                        print("login resepsionis berhasil")
                        os.system('pause') # menu_resepsionis()
                    
                    elif row['role'] == 'admin':
                        detect_user = True
                        temporary( row['id'], row['name'], row['username'], row['password'], row['phone_number'], row['address'], row['religion'], row['gender'], row['place_birth'], row['date_birth'], row['age_category'], row['married'], row['last_education'], row['blood_type'], row['bpjs'], row['role'], row['doctor_category'])
                        log_csv(filelog, username, password, "Berhasil")
                        print("login admin berhasil")           
                        os.system('pause') # menu_admin()
                    
                    else:
                        temporary( row['id'], row['name'], row['username'], row['password'], row['phone_number'], row['address'], row['religion'], row['gender'], row['place_birth'], row['date_birth'], row['age_category'], row['married'], row['last_education'], row['blood_type'], row['bpjs'], row['role'], row['doctor_category'])
                        detect_user = True
                        log_csv(filelog, username, password, "Berhasil")
                        print("login user berhasil")             

                        menu()

                        import dashboard
                        dashboard.menu()
                        return False
           
            if detect_user == False:
                print("Log In Gagal")
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

def temporary( id, name, username, password,phone_number,address,religion,gender,place_birth,date_birth,age_category,married,last_education,blood_type,bpjs,role,doctor_category):
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
        'age_category' : age_category,
        'married' : married,
        'last_education' : last_education,
        'blood_type' : blood_type,
        'bpjs' : bpjs,
        'role' : role,
        'doctor_category' : doctor_category
    }
    return patient_data

