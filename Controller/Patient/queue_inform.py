import csv
import os
from dashboard import menu
import sys
# sys.path.insert(0, 'Controller/Patient/dashboard.py')
# from dashboard import menu

def queue_reader(filename):
    os.system('cls')
    with open(filename, mode='r') as file:
        
        reader = csv.reader(file)

        for row in reader:
            for item in row:
                print(item)

        os.system('pause')
        os.system('cls')    
        menu()

# queue_reader('Database/queue.csv')