import csv
import os
from dashboard_patient import *

def queue_reader(filename, patient_data):
    os.system('cls')
    with open(filename, mode='r') as file:
        
        reader = csv.DictReader(file, delimiter= ';')

        print("\n" + "="*162)
        print(f"{'Id':<5}{'|':<2}{'Nomor Antrian':<14}{'|':<2}{'Id Pasien':<10}{'|':<2}{'Id Dokter':<10}{'|':<2}{'Jenis Pembayaran':<15}{'|':<2}{'Alasan Berkunjung':<19}{'|':<2}{'Deskripsi':<25}{'|':<2}{'Jadwal Periksa':<10}{'|':<2}{'Total Harga':<20}{'|':<2}{'Status':<10}|")
        print("-"*162)
        for row in reader:
            print(f"{row['id']:<5}{'|':<2}{row['queue_number']:<14}{'|':<2}{row['patient_id']:<10}{'|':<2}{row['doctor_id']:<10}{'|':<2}{row['payment_type']:<16}{'|':<3}{row['reason_visit']:<18}{'|':<2}{row['description']:<25}{'|':<2}{row['schedule_checked']:<14}{'|':<2}{row['price_total']:<20}{'|':<2}{row['status']:<10}|")
           
        print("="*162)

        os.system('pause')
        os.system('cls')    
    dashboard_patient.menu_patient(patient_data)
