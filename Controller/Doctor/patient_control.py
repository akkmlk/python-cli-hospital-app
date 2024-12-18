import csv
import sys
sys.path.insert(0, 'C://Document//University//Classroom//Semester1//Alpro//Tugas-Besar//hospital-app//Controller//Increment')
import increment
import dashboard_doctor
# menus = ['Set Jadwal Kontrol', 'Ubah Jadwal']
# for i, j in enumerate(menus):
#     print(f"{i}. {j}")

def patient_control_schedule(doctor_data):
    with open('Database/control.csv', mode='r') as file:
        reader = csv.DictReader(file, delimiter=';')
        control_list = list(reader)

        control_found = False
        for row in control_list:
            if row['doctor_id'] == doctor_data['id']:
                print(row)
                control_found = True
            else:
                control_found = False

        if control_found == False:
            print("Tidak memiliki jadwal kontrol pasien!")

        choosed_choice = input("Kembali ke dashboard? (Y/N) : ").lower()
        while True:
            if choosed_choice == "y":
                dashboard_doctor.menu_doctor(doctor_data)
                return False
            else:
                patient_control_schedule(doctor_data)
                return False

def select_queue_number(doctor_data):
    with open('Database/queue.csv', mode='r') as file:
        reader = csv.DictReader(file, delimiter=';')
        queue_list = list(reader)

    print("\n")
    while True:
        input_queue_number = input("Masukkan nomor antrian : ").lower()
        
        queue_found = False
        for queue in queue_list:
            if queue['queue_number'].lower() == input_queue_number and queue['status'] == "verified":
                queue_found = True
                print(queue)
                add_control_schedule(queue, doctor_data)
                return False
            else:
                queue_found = False

        if queue_found == False:
            print("Nomor antrian tidak ditemukan!")

def add_control_schedule(queue_data, doctor_data):
    while True:
        schedule_selected = input("Masukkan tanggal (format dd-MM-yyyy) : ")
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
                            dashboard_doctor.menu_doctor(doctor_data)
                            return False
                else:
                    print("Room tidak boleh kosong!")
        else:
            print("Jadwal control tidak boleh kosong!")
