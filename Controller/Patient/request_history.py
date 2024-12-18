import csv
import os


def patient_list(filename):
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file, delimiter=';')
 
        print("\n" + "="*172)
        print(f"{'ID':<5}{'|':<2}{'No. Antrian':<20}{'|':<2}{'Patient_ID':<13}{'|':<2}{'Doctor_ID':<12}{'|':<2}{'Jenis Pembayaran':<20}{'|':<2}{'Alasan':<20}{'|':<2}{'Deskripsi':<15}{'|':<2}{'Jadwal':<10}{'|':<2}{'Ruangan':<10}{'|':<2}{'Total':<13}{'|':<2}{'Status':<13}|")
        print("-"*172)

        for row in reader:
            if row['status'] == 'done':
                
                print(f"{row['id']:<5}{'|':<2}{row['queue_number']:<20}{'|':<2}{row['patient_id']:<13}{'|':<2}{row['doctor_id']:<12}{'|':<2}{row['payment_type']:<20}{'|':<2}{row['reason_visit']:<20}{'|':<2}{row['description']:<15}{'|':<2}{row['schedule_checked']:<10}{'|':<2}{row['schedule_checked']:<10}{'|':<2}{row['price_total']:<13}{'|':<2}{row['status']:<13}|")
            else:
                ("data akun tidak tersedia")
    print("="*172)

patient_list('Database/queue.csv')



         
