import os
from patient_control import *

def menu_doctor(doctor_data):
    print(f"Halo Dokter, {doctor_data['name']}")
    os.system('pause')

    menus = ['Keluar', 'Buat jadwal kontrol pasien', "Lihat jadwal kontrol pasien"]
    for i, j in enumerate(menus):
        print(f"{i}. {j}")

    while True:
        choosed_menu = str(input("Pilih menu : "))
        if choosed_menu == "1":
            select_queue_number(doctor_data)
            return False
        elif choosed_menu == "2":
            patient_control_schedule(doctor_data)
            return False
        elif choosed_menu == "0":
            print("keluar")
            return False
        else:
            print("Maaf! Menu tidak tersedia")