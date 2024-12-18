import csv
import os
import sys
sys.path.insert(0, 'C://Document//University//Classroom//Semester1//Alpro//Tugas-Besar//hospital-app//Controller//Increment')
sys.path.insert(0, 'C://Document//University//Classroom//Semester1//Alpro//Tugas-Besar//hospital-app//Controller//Admin')
import increment
import crud_resepsionis_fix
import dashboard_patient

def medical_treatment(patient_data):
    while True:
        schedule_selected = input("Tanggal berapa kamu ingin berobat (format dd-MM-yyyy) : ")
        if schedule_selected != "":
            while True:
                reason_visit = input("Apa keluhan kamu : ")
                if reason_visit != "":
                    description = input("Deskripsikan keluhan kamu (Jika tidak ingin boleh di kosongkan) : ")
                    payment_types = ['CASH', 'BPJS']
                    for i, j in enumerate(payment_types):
                        print(f"{i + 1}. {j}")

                    while True:
                        payment_type_choosed = str(input("Mau bayar pake apa : "))

                        if payment_type_choosed == "1":
                            submit_application(patient_data, schedule_selected, reason_visit, description, "CASH")
                            return False
                        elif payment_type_choosed == "2":
                            while True:
                                bpjs_number = input("Tuliskan nomor BPJS kamu : ")
                                if bpjs_number == "":
                                    print("No BPJS tidak boleh kosong")
                                else:
                                    submit_application(patient_data, schedule_selected, reason_visit, description, bpjs_number)
                                    return False
                        else:
                            print("Silahkan gunakan pembayaran yang tersedia!")
                else:
                    print("Tuliskan keluhan mu disini!")
        else:
            print("Masukkan tanggal yang diinginkan!")

def submit_application(patient_data, schedule_selected, reason_visit, description, payment):
    with open('Database/queue.csv', mode='r') as file:
        reader = csv.DictReader(file, delimiter=';')
        headers = reader.fieldnames

        queue_list = list(reader)

    with open('Database/queue.csv', mode='a', newline='') as write:
        new_queue_data = {
            'id' : increment.id(queue_list),
            'queue_number' : increment.queue_number(queue_list),
            'patient_id' : patient_data['id'],
            'payment_type' : payment,
            'reason_visit' : reason_visit,
            'description' : description,
            'schedule_checked' : schedule_selected,
            'status' : 'waiting',
        }

        writer = csv.DictWriter(write, fieldnames=headers, delimiter=';')
        writer.writerow(new_queue_data)

    print("Pengajuan berhasil dikirim, verifikasi sedang dilakukan!")
    os.system('pause')
    os.system('cls')
    dashboard_patient.menu_patient(patient_data)
