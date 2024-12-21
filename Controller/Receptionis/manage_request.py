import os
import csv
import dashboard_receptionis

def manage_request(filename, receptionis_data):
    with open(filename,mode="r") as file :
        reader = csv.DictReader(file,delimiter=';')
        
        print("\n" + "="*189)
        print(f"{'Nomor Antrian ':<20}{'|':<2}{'ID_Pasien':<20}{'|':<2}{'ID_Dokter':<10}{'|':<2}{'Tipe_Pembayaran':<15}{'|':<2}{'Alasan_berkunjung':<20}{'|':<2}{'Deskripsi':<40}{'|':<2}{'jadwal diperiksa':<10}{'|':<2}{'Harga_total':<10}{'|':<2}{'Status':<20}|")
        print("-"*189)
        for row in reader :
            if row['status'] == ('waiting') :
                print(f"{row['queue_number']:<20}{'|':<2}{row['patient_id']:<20}{'|':<2}{row['doctor_id']:<10}{'|':<2}{row['payment_type']:<15}{'|':<2}{row['reason_visit']:<20}{'|':<2}{row['description']:<40}{'|':<2}{row['schedule_checked']:<16}{'|':<2}{row['price_total']:<11}{'|':<2}{row['status']:<20}|")
                print("="*189)
        choose_request('Database\queue.csv', receptionis_data)
    os.system('pause')

def choose_request(filename, receptionis_data):
    print("Silahkan pilih data yang mau diproses")

    with open(filename,mode='r') as file :
        reader = csv.DictReader(file,delimiter=';')

        patient_list = list(reader)
        while True:
            choosing_data = input(str('Masukan nomor antrian pasien : ')).lower()
            queue_found = False
            for row in patient_list :
                if row['status'] != 'verified' and row['status'] != 'done':
                    if row['queue_number'].lower() == str(choosing_data) :
                        print("\n" + "="*189)
                        print(f"{'Nomor Antrian ':<20}{'|':<2}{'ID_Pasien':<20}{'|':<2}{'ID_Dokter':<10}{'|':<2}{'Tipe_Pembayaran':<15}{'|':<2}{'Alasan_berkunjung':<20}{'|':<2}{'Deskripsi':<40}{'|':<2}{'jadwal diperiksa':<16}{'|':<2}{'Harga_total':<10}{'|':<2}{'Status':<20}|")
                        print("-"*189)
                        print(f"{row['queue_number']:<20}{'|':<2}{row['patient_id']:<20}{'|':<2}{row['doctor_id']:<10}{'|':<2}{row['payment_type']:<15}{'|':<2}{row['reason_visit']:<20}{'|':<2}{row['description']:<40}{'|':<2}{row['schedule_checked']:<16}{'|':<2}{row['price_total']:<11}{'|':<2}{row['status']:<20}|")
                        print("="*189)
                        os.system('pause')
                        print("Ini adalah data dokter yang tersedia ")
                        queue_choosed = row
                        viewing_doctor_data('Database/user.csv', queue_choosed, receptionis_data)
                        queue_found = True
                        return False
                    else:
                        queue_found = False
                else:
                    queue_found = False

            if queue_found == False:
                print("Data tidak tersedia")

def viewing_doctor_data(filename, queue_choosed, receptionis_data):
    with open(filename,mode="r") as file:
        reader = csv.DictReader(file,delimiter=';')
        print("\n" + "="*154)
        print(f"{'ID':<5}{'|':<2}{'Nama':<20}{'|':<2}{'Alamat':<20}{'|':<2}{'Agama':<10}{'|':<2}{'Gender':<15}{'|':<2}{'Tanggal Lahir':<15}{'|':<2}{'Gol Darah':<10}{'|':<2}{'BPJS':<10}{'|':<2}{'Peran':<10}{'|':<2}{'Kategori':<20}|")
        print("-"*154)
        for row in reader :
            if row['role'] == str('doctor'):
                # print(row)
                print(f"{row['id']:<5}{'|':<2}{row['name']:<20}{'|':<2}{row['address']:<20}{'|':<2}{row['religion']:<10}{'|':<2}{row['gender']:<15}{'|':<2}{row['date_birth']:<15}{'|':<2}{row['blood_type']:<10}{'|':<2}{row['bpjs']:<10}{'|':<2}{row['role']:<10}{'|':<2}{row['doctor_category']:<20}|")
        print("="*154)
        choosing_doctor('Database/queue.csv','Database/user.csv', queue_choosed, receptionis_data)

def choosing_doctor(filename,datadokter, queue_choosed, receptionis_data):
    with open(datadokter,mode='r') as baca :
        pembaca = csv.DictReader(baca,delimiter=';')
        item = list(pembaca)
        doctor_found = False
        while True:
            doctor_choosed = input(str("Masukan dokter idnya : "))
            for dokter in item:
                if dokter['role'] == "doctor":
                    if dokter['id'] == doctor_choosed:
                        doctor_found = True
                        print("data ada")
                        update_queue_patient(filename, doctor_choosed, queue_choosed, receptionis_data)
                        return False
                    else:
                        doctor_found = False
                else:
                    doctor_found = False

            if doctor_found == False:
                print("Dokter tidak ada")

def update_queue_patient(filename, doctor_choosed, queue_choosed, receptionis_data):
    with open(filename, mode='r') as read:
        reader = csv.DictReader(read, delimiter=';')
        header = reader.fieldnames

        data = list(reader)

        for row in data:
            if row['queue_number'] == queue_choosed['queue_number']:    
                if row['reason_visit'] != "blood_check" and row['reason_visit'] != "consultation" and row['reason_visit'] != "urine_test":
                    price_total = input("Masukan total harga berobat pasien : ")
                    
                    new_data = {
                        'doctor_id' : doctor_choosed,
                        'status':'verified',
                        'price_total': price_total,
                    }
                    row.update(new_data)
                else:
                    new_data_without_price = {
                        'doctor_id' : doctor_choosed,
                        'status':'verified'
                    }
                    row.update(new_data_without_price)

    with open(filename,mode='w',newline='') as file :
        writer = csv.DictWriter(file,fieldnames=header, delimiter=';') 

        writer.writeheader()
        writer.writerows(data)
    print("Updated")
    os.system('cls')
    dashboard_receptionis.menu_receptionis(receptionis_data)