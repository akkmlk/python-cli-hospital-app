import csv
import os
# from dashboard import menu
# import sys
# sys.path.insert(0, 'D:\New-folder\python-cli-hospital-app\Controller\Patient\dashboard.py')?

def queue_reader(filename):
    os.system('cls')
    with open(filename, mode='r') as file:
        
        reader = csv.reader(file)

        for row in reader:
            for item in row:
                print(item)
                
                # import dashboard

        os.system('pause')
        os.system('cls')    
        # menu()

# queue_reader('Database/queue.csv')