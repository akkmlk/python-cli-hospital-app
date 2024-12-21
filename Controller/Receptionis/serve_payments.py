import os 
import csv
import sys
import dashboard_receptionis

def serve_payment(receptionis_data):
    while True:
        print("1. Menu pembayaran kontrol")
        print("2. Menu pembayaran berobat")
        print("3. Menu pembayaran pemeriksaan medis ")
        penginputan_menu_pembayran = (input(str("Masukan pilihan anda : ")))

        if penginputan_menu_pembayran == "1":
            payment_control('Database/control.csv', receptionis_data)
            return False
        elif penginputan_menu_pembayran == "2":
            payment_code('Database/queue.csv', receptionis_data)
            return False
        elif penginputan_menu_pembayran == "3":
            payment_code('Database/queue.csv', receptionis_data)
            return False
        else:
            print("Mohon masukan pilihan yang ada :")

def payment_control(filename, receptionis_data):
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file, delimiter=';')
        header = reader.fieldnames
        control_data = list(reader)
        control_found = False

        while True:
            control_code = input("Masukkan kode kontrol : ").lower()
            if control_code != "":
                for row in control_data:
                    if row['status'] == "waiting":
                        if row['control_number'].lower() == control_code:
                            print("\n" + "="*125)
                            print(f"{'Nomor Antrian ':<20}{'|':<2}{'ID_Pasien':<20}{'|':<2}{'ID_Dokter':<10}{'|':<2}{'Tipe_Pembayaran':<15}{'|':<2}{'jadwal diperiksa':<16}{'|':<2}{'Harga_total':<10}{'|':<2}{'Status':<20}|")
                            print("-"*125)
                            print(f"{row['control_number']:<20}{'|':<2}{row['patient_id']:<20}{'|':<2}{row['doctor_id']:<10}{'|':<2}{row['payment_type']:<15}{'|':<2}{row['control_schedule']:<16}{'|':<2}{row['price_total']:<11}{'|':<2}{row['status']:<20}|")
                            print("="*125)
                            control_found = True
                            print("Apakah pasien ingin membayar : ")
                            while True:
                                pay = input("(y/n?) : ").lower()
                                if pay == "y": 
                                    if row['payment_type'] == 'CASH':
                                        while True:
                                            jumlah_uang = int(input("Masukan jumlah uang pasien :"))
                                            if jumlah_uang < int(row['price_total']):
                                                print("Uang paisen kurang ")
                                            else:
                                                updated_status = {
                                                    'status':'done'
                                                }

                                                if row['control_number'].lower() == str(control_code):
                                                    row.update(updated_status) 
                                                with open(filename,mode='w',newline='') as write :
                                                    writer = csv.DictWriter(write,fieldnames=header,delimiter=';')

                                                    writer.writeheader()
                                                    writer.writerows(control_data)

                                                print("Pembayaran berhasil dilunasi")
                                                dashboard_receptionis.menu_receptionis(receptionis_data)
                                                return False
                                    else:   
                                        updated_status = {
                                                'status':'done'
                                        }

                                    if row['control_number'].lower() == str(control_code):
                                        row.update(updated_status) 
                                    with open(filename,mode='w',newline='') as write :
                                        writer = csv.DictWriter(write,fieldnames=header,delimiter=';')

                                        writer.writeheader()
                                        writer.writerows(control_data)

                                    print("Pembayaran berhasil dilunasi")
                                    dashboard_receptionis.menu_receptionis(receptionis_data)
                                    return False
                                elif pay == "n":
                                    exit()
                                else:
                                    print("Mohon masukkan input yang sesuai!")
                    else:
                        control_found = False
            else:
                print("Harap masukkan kode nya!")

            if control_found == False:
                print("Data tidak tersedia")

def payment_code(filename, receptionis_data):
    with open(filename,mode='r') as file:
        reader = csv.DictReader(file,delimiter=';')
        header = reader.fieldnames 
        data = list(reader)
        queue_found = False
        while True:
            kode = input(str("Masukan kode antrian : ")).lower()
            for row in data:
                if row['status'] == "verified":
                    if row['queue_number'].lower() == kode:
                        print("\n" + "="*189)
                        print(f"{'Nomor Antrian ':<20}{'|':<2}{'ID_Pasien':<20}{'|':<2}{'ID_Dokter':<10}{'|':<2}{'Tipe_Pembayaran':<15}{'|':<2}{'Alasan_berkunjung':<20}{'|':<2}{'Deskripsi':<40}{'|':<2}{'jadwal diperiksa':<16}{'|':<2}{'Harga_total':<10}{'|':<2}{'Status':<20}|")
                        print("-"*189)
                        print(f"{row['queue_number']:<20}{'|':<2}{row['patient_id']:<20}{'|':<2}{row['doctor_id']:<10}{'|':<2}{row['payment_type']:<15}{'|':<2}{row['reason_visit']:<20}{'|':<2}{row['description']:<40}{'|':<2}{row['schedule_checked']:<16}{'|':<2}{row['price_total']:<11}{'|':<2}{row['status']:<20}|")
                        print("="*189)
                        queue_found = True
                        print("Apakah pasien ingin membayar : ")
                        while True:
                            pay = input("(y/n?) : ").lower()
                            if pay == "y": 
                                if row['payment_type'] == 'CASH':
                                    while True:
                                        jumlah_uang = int(input("Masukan jumlah uang pasien :"))
                                        if jumlah_uang < int(row['price_total']):
                                            print("Uang paisen kurang ")
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

                                            print(f"Pembayaran berhasil dilunasi. Kembalian Rp.{jumlah_uang - int(row['price_total'])}")
                                            dashboard_receptionis.menu_receptionis(receptionis_data)
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

                                    print("Pembayaran berhasil dilunasi")
                                    dashboard_receptionis.menu_receptionis(receptionis_data)
                                    return False
                            elif pay == "n":
                                exit()
                            else:
                                print("Mohon masukan input yang sesuai ")
                else:
                    queue_found = False

            if queue_found == False:
                print("Data tidak tersedia")