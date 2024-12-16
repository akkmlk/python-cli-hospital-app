import os 
import csv
import sys

def serve_payment():
    while True:
        print("1. menu pembayaran kontrol")
        print("2. menu pembayaran berobat")
        print("3. menu pembayaran pemeriksaan medis ")
        penginputan_menu_pembayran = (input(str("masukan pilihan anda : ")))

        if penginputan_menu_pembayran == "1":
            payment_code('Database/queue.csv')
            return False
        elif penginputan_menu_pembayran == "2":
            payment_code('Database/queue.csv')
            return False
        elif penginputan_menu_pembayran == "3":
            payment_code('Database/queue.csv')
            return False
        else:
            print("mohon masukan pilihan yang ada :")


def payment_code(filename):
    with open(filename,mode='r') as file:
        reader = csv.DictReader(file,delimiter=';')
        header = reader.fieldnames 
        data = list(reader)
        while True:
            kode = input(str('masukan kode pembayaran : '))
            queue_found = False
            for row in data:
                if row['queue_number'] == kode:
                    print(row)
                    queue_found = True
                    print("apakah pasien ingin membayar : ")
                    pay = input("(y/n?) : ").lower()    
                    
                    if pay == "y": 
                            
                            data_yangditambah = {
                                'status':'done'
                            }    
                            if row['queue_number'] == str(kode):
                                row.update(data_yangditambah) 
                            with open(filename,mode='w',newline='') as file :
                                writer = csv.DictWriter(file,fieldnames=header,delimiter=';')

                                writer.writeheader()
                                writer.writerows(data)
                    else:
                        exit()  
                    return False
                else:
                    queue_found = False

            if queue_found == False:
                print("data tidak tersedia")
                
            

serve_payment()




