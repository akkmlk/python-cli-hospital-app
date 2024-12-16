import csv
import os
from dashboard_patient import *

def queue_reader(filename, patient_data):
    os.system('cls')
    with open(filename, mode='r') as file:
        
        reader = csv.reader(file)

        for row in reader:
            for item in row:
                print(item)

        os.system('pause')
        os.system('cls')    
    dashboard_patient.menu_patient(patient_data)