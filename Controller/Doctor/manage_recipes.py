import csv
import os
import dashboard_doctor

def input_medicine_recipe(queue_data, doctor_data):
    medicine_list = []
    with open('Database/recipe.csv', mode='r') as file:
        reader = csv.DictReader(file, delimiter=';')
        headers = reader.fieldnames
        recipe_list = list(reader)
        if len(recipe_list) == 0:
            id = 1
        else:
            id = int(recipe_list[-1]['id']) + 1
    while True:
        medicine_name = input("Masukkan nama obat : ")
        medicine_list.append({
            'id' : id,
            'queue_number' : queue_data['queue_number'],
            'medicine_name' : medicine_name
        })
        id += 1
        question = input("Obatnya sudah cukup? (Y/N) : ").lower()
        if question == "y":
            create_medicine_recipe(medicine_list, headers, doctor_data)
            return False
        else:
            print("Silahkan tambah obat lainnya")

def create_medicine_recipe(medicine_list, headers, doctor_data):
    # print(medicine_list)
    with open('Database/recipe.csv', mode='a', newline='') as write:
        writer = csv.DictWriter(write, fieldnames=headers, delimiter=';')
        writer.writerows(medicine_list)
    print("Resep berhasil dibuat!")
    os.system('cls')
    dashboard_doctor.menu_doctor(doctor_data)