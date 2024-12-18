import os
import csv




def manage_request(filename):
    with open(filename,mode="r") as file :
        reader = csv.DictReader(file,delimiter=';')
        
        print("\n" + "="*171)
        print(f"{'Nomor Antrian ':<20}{'|':<2}{'ID_Pasien':<20}{'|':<2}{'ID_Dokter':<10}{'|':<2}{'Tipe_Pembayaran':<15}{'|':<2}{'Alasan_berkunjung':<15}{'|':<2}{'Deskripsi':<15}{'|':<2}{'jadwal diperiksa':<10}{'|':<2}{'Ruangan':<10}{'|':<2}{'Harga_total':<10}{'|':<2}{'Status':<20}|")
        print("-"*171)
        for row in reader :
            if row['status'] == ('waiting') :
                print(f"{row['queue_number']:<20}{'|':<2}{row['patient_id']:<20}{'|':<2}{row['doctor_id']:<10}{'|':<2}{row['payment_type']:<15}{'|':<2}{row['reason_visit']:<16}{'|':<2}{row['description']:<17}{'|':<2}{row['schedule_checked']:<16}{'|':<2}{row['room']:<10}{'|':<2}{row['price_total']:<10}{'|':<2}{row['status']:<20}|")
                print("="*171)
        choose_request('Database\queue.csv')
        choosing_doctor('Database/queue.csv','Database/user.csv')
    os.system('pause')
# manage_request('Database/queue.csv')

def choose_request(filename):

    print("silahkan pilih data yang mau diproses")
    

    with open(filename,mode='r') as file :
        reader = csv.DictReader(file,delimiter=';')

        patient_list = list(reader)
        while True:
            choosing_data = input(str('masukan nomor queue number pasien : '))
            queue_found = False
            os.system('pause')
            for row in patient_list :
                print("\n" + "="*171)
                print(f"{'Nomor Antrian ':<20}{'|':<2}{'ID_Pasien':<20}{'|':<2}{'ID_Dokter':<10}{'|':<2}{'Tipe_Pembayaran':<15}{'|':<2}{'Alasan_berkunjung':<15}{'|':<2}{'Deskripsi':<15}{'|':<2}{'jadwal diperiksa':<10}{'|':<2}{'Ruangan':<10}{'|':<2}{'Harga_total':<10}{'|':<2}{'Status':<20}|")
                print("-"*171)
                if row['queue_number'] == str(choosing_data) :
                    # print(row)
                    print(f"{row['queue_number']:<20}{'|':<2}{row['patient_id']:<20}{'|':<2}{row['doctor_id']:<20}{'|':<2}{row['payment_type']:<20}{row['reason_visit']:<20}{row['schedule_checked']:<20}{row['price_total']:<20}{row['status']:<20}")
                    print("="*171)
                    os.system('pause')
                    print("ini adalah data dokter yang tersedia ")
                    viewing_doctor_data('Database/user.csv')
                    queue_found = True
                    return False
                else:
                    queue_found = False

            if queue_found == False:
                print("data tidak tersedia")
    os.system('pause')




def viewing_doctor_data(filename):
    with open(filename,mode="r") as file:
        reader = csv.DictReader(file,delimiter=';')
        print("\n" + "="*171)
        print(f"{'ID':<5}{'|':<2}{'Nama':<20}{'|':<2}{'Alamat':<20}{'|':<2}{'Agama':<10}{'|':<2}{'Gender':<15}{'|':<2}{'Tanggal Lahir':<15}{'|':<2}{'Usia':<15}{'|':<2}{'Gol Darah':<10}{'|':<2}{'BPJS':<10}{'|':<2}{'Peran':<10}{'|':<2}{'Kategori':<20}|")
        print("-"*171)
        for row in reader :
            if row['role'] == str('Dokter'):
                # print(row)
                print(f"{row['id']:<5}{'|':<2}{row['name']:<20}{'|':<2}{row['address']:<20}{'|':<2}{row['religion']:<10}{'|':<2}{row['gender']:<15}{'|':<2}{row['date_birth']:<15}{'|':<2}{row['age_category']:<15}{'|':<2}{row['blood_type']:<10}{'|':<2}{row['bpjs']:<10}{'|':<2}{row['role']:<10}{'|':<2}{row['category']:<20}|")
        print("="*171)

# choose_request('Database\queue.csv')


def choosing_doctor(filename,datadokter):
    with open(filename,mode='r') as file :
        reader = csv.DictReader(file,delimiter=';')  

        header = reader.fieldnames  
        data = list(reader)
    with open(datadokter,mode='r') as baca :
        pembaca = csv.DictReader(baca,delimiter=';')

        
        item = list(pembaca)
        while True:
            id_pasien = input("masukan id pasien yang mau ditambahkan dokternya : ")
            menginput_dokter = input(str("masukan dokter idnya : "))
            for row in data :
                if row['id'] == str(id_pasien):
                    for dokter in item:
                        inputing_pricetotal = input("masukan total harga berobat pasien :")
                        data_yangdiubah ={
                            'doctor_id':menginput_dokter,
                            'status':'verified',
                            'price_total': inputing_pricetotal
                        }
                        if dokter['id'] == str(menginput_dokter):
                                row.update(data_yangdiubah)
                                with open(filename,mode='w',newline='') as file :
                                    writer = csv.DictWriter(file,fieldnames=header,delimiter=';')

                                    writer.writeheader()
                                    writer.writerows(data)
                                    print("data telah diubah! ")
                                    return False
                        else:
                            print("data dokter tidak ada ")
                else:
                    print("data pasien tidak ada ")

                


# choosing_doctor('Database/queue.csv','Database/user.csv')