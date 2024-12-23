import os
from medical_treatment import *
from medical_checkup import *
from control import *
from request_history import patient_list
from queue_inform import queue_reader
from update_biodata import update
import sys
sys.path.insert(0, 'C://Document//University//Classroom//Semester1//Alpro//Tugas-Besar//hospital-app//Controller//Login')

def menu_patient(patient_data):
    print(f"Halo Pasien, {patient_data['name']}")
    os.system('pause')

    menu = ['Keluar', 'Berobat', 'Pemeriksaan Kesehatan (Medical Checkup)', 'Kontrol', 'Informasi Antrian', 'Riwayat Pengajuan', 'Biodata']
    for i, j in enumerate(menu):
        print(f"{i}. {j}")

    while True:
        choosed_menu = input("Pilih menu : ")
        if choosed_menu == "1":
            medical_treatment(patient_data)
            return False
        elif choosed_menu == "2":
            menu_medical_checkup(patient_data)
            return False
        elif choosed_menu == "3":
            show_control(patient_data)
            return False
        elif choosed_menu == "4":
            queue_reader('Database/queue.csv', patient_data)
            return False
        elif choosed_menu == "5":
            patient_list('Database/queue.csv', patient_data)
            return False
        elif choosed_menu == "6":
            update('Database/user.csv', patient_data)
            return False
        elif choosed_menu == "0":
            import login
            login.login()
            return False
        else:
            print("Oops! Menu tidak tersedia")
            os.system('pause')