import csv
import os

def read_csv(filename):
    os.system('cls')
    with open(filename, mode='r') as file:
        
        reader = csv.reader(file)

        for row in reader:
            for item in row:
                print(item)

        os.system('pause')
        os.system('cls') # menu_user()

read_csv('Database/queue.csv')