import os 
import csv
from manage_request import *
from serve_payments import *


def menu_resepsionis():
    while True:
        print("menu")
        print("1.mengelola pengajuan ")
        print("2.melayani pembayaran ")
        print("3.keluar ")
        choosing_menu = input(str("masukan pilihan yang tersedia : "))
        if choosing_menu == "1":
            manage_request('Database/queue.csv')
            return False
        elif choosing_menu == "2":
            serve_payment()
            return False
        elif choosing_menu == "3":
            exit()
        else:
            print("silahkan masukan pilihan yang tersedia")

menu_resepsionis()