import sys
from manage_request import *
from serve_payments import *
sys.path.insert(0, 'C://Document//University//Classroom//Semester1//Alpro//Tugas-Besar//hospital-app//Controller//Login')

def menu_receptionis(receptionis_data):
    while True:
        print("1. Mengelola pengajuan ")
        print("2. Melayani pembayaran ")
        print("3. Keluar ")
        choosing_menu = input(str("masukan pilihan yang tersedia : "))
        if choosing_menu == "1":
            manage_request('Database/queue.csv')
            return False
        elif choosing_menu == "2":
            serve_payment()
            return False
        elif choosing_menu == "3":
            import login
            login.login()
        else:
            print("silahkan masukan pilihan yang tersedia")