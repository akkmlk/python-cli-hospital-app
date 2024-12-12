import csv
import datetime

def medical_treatment():
    patient_id = 1

    while True:
        schedule_selected = input("Tanggal berapa kamu ingin berobat (format dd-MM-yyyy) : ")
        if schedule_selected != "":
            while True:
                reason_visit = input("Apa keluhan kamu : ")
                if reason_visit != "":
                    while True:
                        description = input("Deskripsikan keluhan kamu (Jika tidak ingin mendeskripsikan gunakan '-') : ")
                        if description != "":
                            payment_types = ['CASH', 'BPJS']
                            for i, j in enumerate(payment_types):
                                print(f"{i + 1}. {j}")

                            while True:
                                payment_type_choosed = str(input("Mau bayar pake apa : "))

                                if payment_type_choosed == "1":
                                    submit_application(patient_id, schedule_selected, reason_visit, description, "CASH")
                                    return False
                                elif payment_type_choosed == "2":
                                    bpjs_number = input("Tuliskan nomor BPJS kamu : ")
                                    submit_application(patient_id, schedule_selected, reason_visit, description, bpjs_number)
                                    return False
                                else:
                                    print("Silahkan gunakan pembayaran yang tersedia!")
                        else:
                            print("Silahkan gunakan '-'")
                else:
                    print("Tuliskan keluhan mu disini!")
        else:
            print("Masukkan tanggal yang diinginkan!")

def submit_application(patient, schedule_selected, reason_visit, description, payment):
    with open('Database/queue.csv', mode='r') as file:
        reader = csv.DictReader(file, delimiter=';')

        queue_list = list(reader)

        if len(queue_list) == 0:
            queue_id = 1
            queue_number = "AJU" + "001"
        else:
            # for i in queue_list[-1]:
            recent_queue_id = queue_list[-1]['id']
            recent_queue_number = queue_list[-1]['queue_number']
            increment_number = int(recent_queue_number[-3:]) + 1
            queue_number = "AJU" + f"{increment_number:03}"
            queue_id = int(recent_queue_id) + 1


    with open('Database/queue.csv', mode='a', newline='') as write:
        new_queue_data = {
            'id' : queue_id,
            'queue_number' : queue_number,
            'payment_type' : payment,
            'reason_visit' : reason_visit,
            'description' : description,
            'schedule_checked' : schedule_selected,
            'status' : 'waiting',
        }

        writer = csv.DictWriter(write, fieldnames=reader.fieldnames, delimiter=';')
        writer.writerow(new_queue_data)

    print("Pengajuan berhasil dikirim, verifikasi sedang dilakukan!")