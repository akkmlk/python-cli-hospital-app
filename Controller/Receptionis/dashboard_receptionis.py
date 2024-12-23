import sys
from manage_request import manage_request
from serve_payments import serve_payment
sys.path.insert(0, 'C://tugas ngoding//python-cli-hospital-app//Controller//Login')

def menu_receptionis(receptionis_data):
    print(f"Halo Resepsionis, {receptionis_data['name']}")
    while True:
        print("1. Mengelola pengajuan ")
        print("2. Melayani pembayaran ")
        print("3. Keluar ")
        choosing_menu = input(str("masukan pilihan yang tersedia : "))
        if choosing_menu == "1":
            manage_request('Database/queue.csv', receptionis_data)
            return False
        elif choosing_menu == "2":
            serve_payment(receptionis_data)
            return False
        elif choosing_menu == "3":
            import login
            login.login()
        else:
            print("Silahkan masukan pilihan yang tersedia")