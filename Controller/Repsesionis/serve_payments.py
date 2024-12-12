import os 
import csv
import sys

def melayani_pembayran():
    while True:
        print("1. menu pembayaran kontrol")
        print("2. menu pembayaran berobat")
        print("3. menu pembayaran pemeriksaan medis ")
        penginputan_menu_pembayran = (input(str("masukan pilihan anda : ")))

        if penginputan_menu_pembayran == "1":
            pembayaran_kontrol('Database/queue.csv')
            return False
        elif penginputan_menu_pembayran == "2":
            pembayaran_kontrol('Database/queue.csv')
            return False
        elif penginputan_menu_pembayran == "3":
            pembayaran_kontrol('Database/queue.csv')
            return False
        else:
            print("mohon masukan pilihan yang ada :")


def pembayaran_kontrol(filename):
    with open(filename,mode='r') as file:
        kode = input(str('masukan kode pembayaran'))

        reader = csv.DictReader(file,delimiter=';')
        header = reader.fieldnames 
        data = list(reader)
        
        for row in data:
            if row['queue_number'] == kode:
                print(row)
        print("apakah pasien ingin membayar : ")

        bayar = input("y/n?")     
        
        if bayar == "y":
            for row in data: #mengakses setip baris data 
                
                data_yangditambah = {
                    'status':'done'
                }    
                if row['queue_number'] == str(kode):
                    row.update(data_yangditambah) 
        else:
            exit()           
    with open(filename,mode='w',newline='') as file :
        writer = csv.DictWriter(file,fieldnames=header,delimiter=';')

        writer.writeheader()
        writer.writerows(data)

melayani_pembayran()




