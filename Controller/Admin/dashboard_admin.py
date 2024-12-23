import os
import sys
from crud_dokter_fix import *
from crud_resepsionis_fix import *
sys.path.insert(0, 'C://tugas ngoding//python-cli-hospital-app//Controller//Login')

def menu_admin(admin_data):
    print(f"Halo Admin, {admin_data['name']}")
    os.system('pause')

    menus = ['Keluar', 'Crud Dokter', "Crud Resepsionis"]
    for i, j in enumerate(menus):
        print(f"{i}. {j}")

    while True:
        choosed_menu = str(input("Pilih menu : "))
        if choosed_menu == "1":
            main_doctor(admin_data)
            return False
        elif choosed_menu == "2":
            main_resepsionis(admin_data)
            return False
        elif choosed_menu == "0":
            import login
            login.login()
            return False
        else:
            print("Oops! Menu tidak tersedia")