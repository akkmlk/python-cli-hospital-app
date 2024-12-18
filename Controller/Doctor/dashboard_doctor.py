import os
import sys
sys.path.insert(0, 'C://Document//University//Classroom//Semester1//Alpro//Tugas-Besar//hospital-app//Controller//Login')
from patient_control import *

def menu_doctor(doctor_data):
    print(f"Halo Dokter, {doctor_data['name']}")
    os.system('pause')

    menus = ['Keluar', 'Buat jadwal kontrol pasien', "Buat resep obat pasien", "Lihat jadwal kontrol pasien"]
    for i, j in enumerate(menus):
        print(f"{i}. {j}")

    while True:
        choosed_menu = str(input("Pilih menu : "))
        if choosed_menu == "1":
            select_queue_number(doctor_data, "control")
            return False
        elif choosed_menu == "2":
            select_queue_number(doctor_data, "recipe")
            return False
        elif choosed_menu == "3":
            patient_control_schedule(doctor_data)
            return False
        elif choosed_menu == "0":
            import login
            login.login()
            return False
        else:
            print("Maaf! Menu tidak tersedia")