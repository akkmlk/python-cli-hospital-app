import csv
import sys
import os
sys.path.insert(0, 'C://Document//University//Classroom//Semester1//Alpro//Tugas-Besar//hospital-app//Controller//Increment')
sys.path.insert(0, 'C://Document//University//Classroom//Semester1//Alpro//Tugas-Besar//hospital-app//Controller//Admin')
import crud_dokter_fix
import increment
import dashboard_doctor
from manage_recipes import input_medicine_recipe

def patient_control_schedule(doctor_data):
    with open('Database/control.csv', mode='r') as file:
        reader = csv.DictReader(file, delimiter=';')
        control_list = list(reader)

        control_found = False
        print("\n" + "="*109)
        print(f"{'Nomor Kontrol':<20}{'|':<2}{'ID Pasien':<20}{'|':<2}{'ID Dokter':<20}{'|':<2}{'Jadwal Kontrol':<20}{'|':<2}{'Ruangan':<20}|")
        print("-"*109)
        for row in control_list:
            if row['doctor_id'] == doctor_data['id']:
                print(f"{row['control_number']:<20}{'|':<2}{row['patient_id']:<20}{'|':<2}{row['doctor_id']:<20}{'|':<2}{row['control_schedule']:<20}{'|':<2}{row['room']:<20}|")
                control_found = True
            else:
                control_found = False
        print("="*109)

        if control_found == False:
            print("Tidak memiliki jadwal kontrol pasien!")
        
    os.system('pause')
    os.system('cls')
    dashboard_doctor.menu_doctor(doctor_data)

def select_queue_number(doctor_data, option):
    with open('Database/queue.csv', mode='r') as file:
        reader = csv.DictReader(file, delimiter=';')
        queue_list = list(reader)

    while True:
        input_queue_number = input("Masukkan nomor antrian : ").lower()
        
        print("\n" + "="*171)
        print(f"{'Nomor Antrian':<20}{'|':<2}{'ID Pasien':<20}{'|':<2}{'ID Dokter':<20}{'|':<2}{'Tipe Pembayaran':<20}{'Alasan Kunjungan':<20}{'Jadwal Pemeriksaan':<20}{'Total Harga':<20}{'Status':<20}")
        print("-"*171)
        queue_found = False
        for queue in queue_list:
            if queue['queue_number'].lower() == input_queue_number and queue['status'] == "verified":
                queue_found = True
                print(f"{queue['queue_number']:<20}{'|':<2}{queue['patient_id']:<20}{'|':<2}{queue['doctor_id']:<20}{'|':<2}{queue['payment_type']:<20}{queue['reason_visit']:<20}{queue['schedule_checked']:<20}{queue['price_total']:<20}{queue['status']:<20}")
                print("="*171)

                if option == "control":
                    add_control_schedule(queue, doctor_data)
                else:
                    input_medicine_recipe(queue, doctor_data)
                return False
            else:
                queue_found = False

        if queue_found == False:
            print("="*171)
            print("Nomor antrian tidak ditemukan!")

def add_control_schedule(queue_data, doctor_data):
    while True:
        schedule_selected = crud_dokter_fix.validate_date(input("Masukkan tanggal (format dd-MM-yyyy) : "))
        if schedule_selected != "":
            while True:
                room_selected = input("Masukkan ruangan : ")
                if room_selected != "":
                    with open('Database/control.csv', mode='r') as file:
                        reader = csv.DictReader(file, delimiter=';')
                        headers = reader.fieldnames
                        control_list = list(reader)

                    with open('Database/control.csv', mode='a', newline='') as write:
                        writer = csv.DictWriter(write, fieldnames=headers, delimiter=';')

                        new_data_control = {
                            'id' : increment.id(control_list),
                            'control_number' : increment.control_number(control_list),
                            'doctor_id' : queue_data['doctor_id'],
                            'patient_id' : queue_data['patient_id'],
                            'control_schedule' : schedule_selected,
                            'room' : room_selected
                        }
                        writer.writerow(new_data_control)
                    print("Jadwal control berhasil dibuat!\n")

                    choosed_choice = input("Buat jadwal lagi? (Y/N) : ").lower()
                    while True:
                        if choosed_choice == "y":
                            add_control_schedule(queue_data, doctor_data)
                            return False
                        else:
                            os.system('cls')
                            dashboard_doctor.menu_doctor(doctor_data)
                            return False
                else:
                    print("Room tidak boleh kosong!")
        else:
            print("Jadwal control tidak boleh kosong!")
