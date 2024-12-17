import csv
import os

def queue_reader(filename):
    os.system('cls')
    with open(filename, mode='r') as file:
        
        reader = csv.DictReader(file, delimiter= ';')

        print("\n" + "="*164)
        print(f"{'Id':<5}{'|':<2}{'Nomor Antrian':<14}{'|':<2}{'Id Pasien':<10}{'|':<2}{'Id Dokter':<10}{'|':<2}{'Jenis Pembayaran':<15}{'|':<2}{'Alasan Berkunjung':<19}{'|':<2}{'Deskripsi':<15}{'|':<2}{'Jadwal Periksa':<10}{'|':<2}{'Ruang':<10}{'|':<2}{'Total Harga':<20}{'|':<2}{'Status':<10}|")
        print("-"*164)
        for row in reader:
            print(f"{row['id']:<5}{'|':<2}{row['queue_number']:<14}{'|':<2}{row['patient_id']:<10}{'|':<2}{row['doctor_id']:<10}{'|':<2}{row['payment_type']:<16}{'|':<3}{row['reason_visit']:<18}{'|':<2}{row['description']:<15}{'|':<2}{row['schedule_checked']:<14}{'|':<2}{row['room']:<10}{'|':<2}{row['price_total']:<20}{'|':<2}{row['status']:<10}|")
           
        print("="*164)

        os.system('pause')

queue_reader('Database/queue.csv')

# for row in reader:
        #     for item in row:
        #         print(item)
         # print(f"{row[0]:<5}{'|':<2}{row[1]:<20}{'|':<2}{row[2]:<20}{'|':<2}{row[3]:<10}{'|':<2}{row[4]:<15}{'|':<2}{row[5]:<15}{'|':<2}{row[6]:<15}{'|':<2}{row[7]:<10}{'|':<2}{row[8]:<10}{'|':<2}{row[9]:<20}{'|':<2}{row[10]:<20}|")
                