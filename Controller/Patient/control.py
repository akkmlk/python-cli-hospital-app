import csv
import dashboard_patient

def show_control(patient_data):
    with open('Database/control.csv', mode='r') as file:
        reader = csv.DictReader(file, delimiter=';')
        control_list = list(reader)

        control_found = False
        for row in control_list:
            if row['patient_id'] == patient_data['id']:
                print(row)
                control_found = True
            else:
                control_found = False

        if control_found == False:
            print("Kamu tidak memiliki jadwal kontrol!")

        choosed_choice = input("Kembali ke dashboard? (Y/N) : ").lower()
        while True:
            if choosed_choice == "y":
                dashboard_patient.menu_patient(patient_data)
                return False
            else:
                show_control(patient_data)
                return False