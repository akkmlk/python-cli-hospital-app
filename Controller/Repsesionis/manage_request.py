import os
import csv
import sys
# status masih waiting, verified,done 

def mengelola_pengajauan(filename):
    with open(filename,mode="r") as file :
        reader = csv.DictReader(file,delimiter=';')
        
        for row in reader :
            if row['status'] == ('waiting') :
                print(row)

    os.system('pause')
# mengelola_pengajauan('Database/queue.csv')

def memilih_pengajuan(filename):

    print("silahkan pilih data yang mau diproses")
    memilih_data =  input(str('masukan nomor queue number pasien : '))

    with open(filename,mode='r') as file :
        reader = csv.DictReader(file,delimiter=';')

        for row in reader :
            if row['queue_number'] == str(memilih_data) :
                print(row)
                print("ini adalah data dokter yang tersedia ")
                menampilakan_data_dokter('Database/user.csv')
    os.system('pause')




def menampilakan_data_dokter(filename):
    with open(filename,mode="r") as file:
        reader = csv.DictReader(file,delimiter=';')

        for row in reader :
            if row['role'] == str('doctor'):
                print(row)


# memilih_pengajuan('Database\queue.csv')

def menentukan_dokter(filename,data_yangditambah,id_pasien):
    with open(filename,mode='r') as file :
        reader = csv.DictReader(file,delimiter=';') #baca file csv 

        header = reader.fieldnames #secure header 
        data = list(reader)#mengubah reader menjadi data list
        # print(data)
        for row in data: #mengakses setip baris data 
            if row['id'] == str(id_pasien):
                row.update(data_yangditambah)
                # print(data)
    with open(filename,mode='w',newline='') as file :
        writer = csv.DictWriter(file,fieldnames=header,delimiter=';')# membutuhkan 2 parameter, header = kenapa menggunakan hedaer karena dalam data kita sudah memiliki header sendiri 

        writer.writeheader()
        writer.writerows(data)

id_pasien = input("masukan id pasien yang mau ditambahkan dokternya  ")
menginput_dokter = input(str("masukan dokter idnya "))

data_yangditambah ={
    'doctor_id':menginput_dokter,
    'status':'verifikasi'
}

menentukan_dokter('Database/queue.csv',data_yangditambah,id_pasien)