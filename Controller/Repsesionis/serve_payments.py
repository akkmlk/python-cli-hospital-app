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
        kode = input(str('masukan kode pembayaran : ')).lower()
        while True:
            queue_found = False
            for row in data:
                print("\n" + "="*171)
                print(f"{'Nomor Antrian ':<20}{'|':<2}{'ID_Pasien':<20}{'|':<2}{'ID_Dokter':<10}{'|':<2}{'Tipe_Pembayaran':<15}{'|':<2}{'Alasan_berkunjung':<15}{'|':<2}{'Deskripsi':<15}{'|':<2}{'jadwal diperiksa':<10}{'|':<2}{'Ruangan':<10}{'|':<2}{'Harga_total':<10}{'|':<2}{'Status':<20}|")
                print("-"*171)
                if row['queue_number'].lower() == kode:
                    print(f"{row['queue_number']:<20}{'|':<2}{row['patient_id']:<20}{'|':<2}{row['doctor_id']:<10}{'|':<2}{row['payment_type']:<15}{'|':<2}{row['reason_visit']:<16}{'|':<2}{row['description']:<17}{'|':<2}{row['schedule_checked']:<16}{'|':<2}{row['room']:<10}{'|':<2}{row['price_total']:<10}{'|':<2}{row['status']:<20}|")
                    print("="*171)
                    queue_found = True
                    print("apakah pasien ingin membayar : ")
                    pay = input("(y/n?) : ").lower()
                    if pay == "y": 
                        if row['payment_type'] == str('cash'):
                                jumlah_uang = int(input("masukan jumlah uang pasien :"))
                                if jumlah_uang < int(row['price_total']):
                                    print("uang paisen kurang ")
                                    return False
                                else:
                                    data_yangditambah = {
                                        'status':'done'
                                    }    
                                    if row['queue_number'] == str(kode):
                                        row.update(data_yangditambah) 
                                    with open(filename,mode='w',newline='') as file :
                                        writer = csv.DictWriter(file,fieldnames=header,delimiter=';')

                                        writer.writeheader()
                                        writer.writerows(data)
                                        return False
                        else:    
                            data_yangditambah = {
                                    'status':'done',
                            }    
                            if row['queue_number'] == str(kode):
                                row.update(data_yangditambah) 
                            with open(filename,mode='w',newline='') as file :
                                writer = csv.DictWriter(file,fieldnames=header,delimiter=';')

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
                
            





