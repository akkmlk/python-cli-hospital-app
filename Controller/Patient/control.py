import csv
import os
import dashboard_patient

def show_control(patient_data):
    with open('Database/control.csv', mode='r') as file:
        reader = csv.DictReader(file, delimiter=';')
        control_list = list(reader)

        control_found = False
        print("\n" + "="*171)
        print(f"{'Nomor Kontrol':<20}{'|':<2}{'ID Pasien':<20}{'|':<2}{'ID Dokter':<20}{'|':<2}{'Jadwal Kontrol':<20}{'Ruangan':<20}")
        print("-"*171)
        for row in control_list:
            if row['patient_id'] == patient_data['id']:
                control_found = True
                print(f"{row['control_number']:<20}{'|':<2}{row['patient_id']:<20}{'|':<2}{row['doctor_id']:<20}{'|':<2}{row['control_schedule']:<20}{row['room']:<20}")
        print("="*171)

        if control_found == False:
            print("Kamu tidak memiliki jadwal kontrol!")

        choosed_choice = input("Kembali ke dashboard? (Y/N) : ").lower()
        while True:
            if choosed_choice == "y":
                os.system('cls')
                dashboard_patient.menu_patient(patient_data)
                return False
            else:
                show_control(patient_data)
                return False
            
            