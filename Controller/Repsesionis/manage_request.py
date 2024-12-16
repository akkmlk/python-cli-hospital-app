import os
import csv
import sys



def manage_request(filename):
    with open(filename,mode="r") as file :
        reader = csv.DictReader(file,delimiter=';')
        
        for row in reader :
            if row['status'] == ('waiting') :
                print(row)

    os.system('pause')
manage_request('Database/queue.csv')

def choose_request(filename):

    print("silahkan pilih data yang mau diproses")
    

    with open(filename,mode='r') as file :
        reader = csv.DictReader(file,delimiter=';')

        patient_list = list(reader)
        while True:
            choosing_data = input(str('masukan nomor queue number pasien : '))
            queue_found = False
            for row in patient_list :
                if row['queue_number'] == str(choosing_data) :
                    print(row)
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

        for row in reader :
            if row['role'] == str('doctor'):
                print(row)


choose_request('Database\queue.csv')


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
                        data_yangdiubah ={
                            'doctor_id':menginput_dokter,
                            'status':'verified'
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

                


choosing_doctor('Database/queue.csv','Database/user.csv')