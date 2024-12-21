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
            kode = input(str("masukan kode pembayaran : ")).lower()
            queue_found = False
            for row in data:
                if row['status'] == "verified":
                    if row['queue_number'].lower() == kode:
                        print("\n" + "="*189)
                        print(f"{'Nomor Antrian ':<20}{'|':<2}{'ID_Pasien':<20}{'|':<2}{'ID_Dokter':<10}{'|':<2}{'Tipe_Pembayaran':<15}{'|':<2}{'Alasan_berkunjung':<20}{'|':<2}{'Deskripsi':<40}{'|':<2}{'jadwal diperiksa':<16}{'|':<2}{'Harga_total':<10}{'|':<2}{'Status':<20}|")
                        print("-"*189)
                        print(f"{row['queue_number']:<20}{'|':<2}{row['patient_id']:<20}{'|':<2}{row['doctor_id']:<10}{'|':<2}{row['payment_type']:<15}{'|':<2}{row['reason_visit']:<20}{'|':<2}{row['description']:<40}{'|':<2}{row['schedule_checked']:<16}{'|':<2}{row['price_total']:<11}{'|':<2}{row['status']:<20}|")
                        print("="*189)
                        queue_found = True
                        print("apakah pasien ingin membayar : ")
                        pay = input("(y/n?) : ").lower()
                        if pay == "y": 
                            if row['payment_type'] == 'CASH':
                                jumlah_uang = int(input("masukan jumlah uang pasien :"))
                                if jumlah_uang < int(row['price_total']):
                                    print("uang paisen kurang ")
                                else:
                                    data_yangditambah = {
                                        'status':'done'
                                    }    
                                    if row['queue_number'].lower() == str(kode):
                                        row.update(data_yangditambah) 
                                    with open(filename,mode='w',newline='') as file :
                                        writer = csv.DictWriter(file,fieldnames=header,delimiter=';')

                                        writer.writeheader()
                                        writer.writerows(data)
                                        return False
                            else:   
                                data_yangditambah = {
                                        'status':'done'
                                }    
                                if row['queue_number'].lower() == str(kode):
                                    row.update(data_yangditambah) 
                                with open(filename,mode='w',newline='') as write :
                                    writer = csv.DictWriter(write,fieldnames=header,delimiter=';')

                                    writer.writeheader()
                                    writer.writerows(data)
                                    return False
                        elif pay == "n":
                            exit()
                        else:
                            print("mohon masukan input yang sesuai ")
                else:
                    queue_found = False

            if queue_found == False:
                print("data tidak tersedia")
                
            

#