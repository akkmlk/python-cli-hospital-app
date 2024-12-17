import os
from medical_treatment import *

from queue_inform import queue_reader

def menu():
    print(f"Halo Pasien, Akmal Yunus")
    os.system('pause')


    menu = ['Keluar', 'Berobat', 'Pemeriksaan Kesehatan', 'Kontrol', 'Informasi Antrian', 'Riwayat Pengajuan', 'Biodata']
    for i, j in enumerate(menu):
        print(f"{i}. {j}")

    while True:
        choosed_menu = str(input("Pilih menu : "))
        if choosed_menu == "1":
            medical_treatment()
            return False
        elif choosed_menu == "2":
            print("checkup")
            return False
        elif choosed_menu == "3":
            print("kontrol")
            return False
        elif choosed_menu == "4":
            print("antrian")
            # import queue_inform
            queue_reader('Database/queue.csv')
            # return False
            return False
        elif choosed_menu == "5":
            print("riwayat")
            return False
        elif choosed_menu == "6":
            print("biodata")
            return False
        elif choosed_menu == "0":
            print("keluar")
            return False
            
        else:
            print("Oops! Menu tidak tersedia")
            os.system('pause')

menu()