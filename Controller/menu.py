import os 
import csv 
import datetime as dt

otp = 'password'

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
                if username == row['Username'] and password == row[otp]:
                    print("Log In Berhasil")
                    detect_user = True
                    log_csv(filelog, username, password, "Berhasil")
                    os.system('pause')

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

login('user.csv', 'Log.csv')
