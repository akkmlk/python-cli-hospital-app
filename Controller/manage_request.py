import os
import csv
import sys
# status masih waiting, verified,done 

def mengelola_pengajauan(filename):
    with open(filename,mode="r") as file :
        reader = csv.DictReader(file,delimiter=';')
        
        # for row in reader :
        #     if row['status'] = {'waiting'}



def menampilakan_data_dokter(filename):
    with open(filename,mode="r") as file:
        reader = csv.DictReader(file)

        for row in reader :
            print(row)

menampilakan_data_dokter("Database/user.csv")