import os
import csv
import sys
sys.path.insert(1, 'C://Document//University//Classroom//Semester1//Alpro//Tugas-Besar//hospital-app//Controller//Increment')
# from Increment.increment_queue import queue_number
# from Increment.increment_queue import queue_id
import increment

def menu_medical_checkup(patient_data):
    menus = ['Cek Darah', 'Tes Urine', 'Konsultasi']

    for i, j in enumerate(menus):
        print(f"{i + 1}. {j}")

    while True:
        choosed_menu = str(input("Pilih menu : "))
        if choosed_menu == "1":
            form("blood_check", patient_data)
            return False
        elif choosed_menu == "2":
            form("urine_test", patient_data)
            return False
        elif choosed_menu == "3":
            form("consultation", patient_data)
            return False
        else:
            print("Oops! Menu tidak tersedia")
            os.system('pause')

def form(reason_visit, patient_data):
    if reason_visit == "blood_check":
        print("Mau cek darah tanggal berapa?")
        price_total = 30000
    elif reason_visit == "urine_test":
        print("Mau tes urine tanggal berapa?")
        price_total = 80000
    elif reason_visit == "consultation":
        print("Mau konsultasi tanggal berapa?")
        price_total = 200000

    while True:
        schedule_selected = str(input("Masukkan tanggal nya (format dd-MM-yyyy) : "))
        
        if schedule_selected != "":
            description = ""
            if reason_visit == "consultation":
                description = str(input("Cerita sedikit yuk soal keluhan kamu (Kalo gamau boleh di kosongin ko) : "))
            
            payment_types = ['CASH', 'BPJS']
            for i, j in enumerate(payment_types):
                print(f"{i + 1}. {j}")

            while True:
                payment_type_choosed = str(input("Mau bayar pake apa? "))
                if payment_type_choosed == "1":
                    submit_application(reason_visit, schedule_selected, description, "CASH", price_total, patient_data)
                    return False
                elif payment_type_choosed == "2":
                    while True:
                        bpjs_number = str(input("Tuliskan nomor BPJS kamu : "))
                        if bpjs_number == "":
                            print("No BPJS tidak boleh kosong")
                        else:
                            submit_application(reason_visit, schedule_selected, description, bpjs_number, price_total, patient_data)
                            return False
                else:
                    print("Silahkan gunakan pembayaran yang tersedia!")
        else:
            print("Masukkan tanggal yang diinginkan!")

def submit_application(reason_visit, schedule_selected, description, payment, price_total, patient_data):
    with open('Database/queue.csv', mode='r', newline='') as file:
        reader = csv.DictReader(file, delimiter=';')
        headers = reader.fieldnames
        queue_list = list(reader)

    with open('Database/queue.csv', mode='a', newline='') as write:
        new_queue_data = {
            'id' : increment.id(queue_list),
            'queue_number' : increment.queue_number(queue_list),
            'patient_id' : patient_data['id'],
            'description' : description,
            'schedule_checked' : schedule_selected,
            'payment_type' : payment,
            'reason_visit' : reason_visit,
            'price_total' : price_total,
            'status' : 'waiting',
        }
        writer = csv.DictWriter(write, fieldnames=headers, delimiter=';')
        writer.writerow(new_queue_data)

    print("Pengajuan berhasil dikirim, verifikasi sedang dilakukan!")