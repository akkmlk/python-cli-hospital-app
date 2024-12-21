import csv
import os
from dashboard_patient import *

def patient_list(filename, patient_data):
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file, delimiter=';')

        print("\n" + "="*192)
        print(f"{'ID':<5}{'|':<2}{'No. Antrian':<20}{'|':<2}{'Patient_ID':<13}{'|':<2}{'Doctor_ID':<12}{'|':<2}{'Jenis Pembayaran':<20}{'|':<2}{'Alasan':<20}{'|':<2}{'Deskripsi':<35}{'|':<2}{'Jadwal':<10}{'|':<2}{'Ruangan':<10}{'|':<2}{'Total':<13}{'|':<2}{'Status':<13}|")
        print("-"*192)

        request_history_found = False
        for row in reader:
            if row['patient_id'] == patient_data['id'] and row['status'] == 'done':
                request_history_found = True
                print(f"{row['id']:<5}{'|':<2}{row['queue_number']:<20}{'|':<2}{row['patient_id']:<13}{'|':<2}{row['doctor_id']:<12}{'|':<2}{row['payment_type']:<20}{'|':<2}{row['reason_visit']:<20}{'|':<2}{row['description']:<35}{'|':<2}{row['schedule_checked']:<10}{'|':<2}{row['schedule_checked']:<10}{'|':<2}{row['price_total']:<13}{'|':<2}{row['status']:<13}|")
            else:
                request_history_found = False
        print("="*192)

        if request_history_found == False:
            print("Tidak memiliki riwayat pengajuan")

    os.system('pause')
    os.system('cls')
    dashboard_patient.menu_patient(patient_data)