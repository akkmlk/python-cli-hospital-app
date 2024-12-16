import csv
import os

def queue_reader(filename):
    os.system('cls')
    with open(filename, mode='r') as file:
        
        reader = csv.reader(file)

        for row in reader:
            for item in row:
                print(item)
                
        os.system('pause')
       
       