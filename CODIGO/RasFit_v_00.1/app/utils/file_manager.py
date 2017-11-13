#!/usr/bin/python3
# -*- coding: utf-8 -*-



import csv



try:
    from app.utils import color
except Exception as e:
    print('FAILED TO IMPORT INNER TOOLS in file_manager.py: ' + str(e))
    exit(1)



def read_csv_dict(file_name):
    data_r = {}
    try:
        with open(file_name, 'r') as f:
            reader = csv.reader(f)
            for line in reader:
                data_r[line[0]] = line[1:]
            
        color.p("[+] SUCCESS: reading " + file_name, "gre")
    except Exception as e:
        color.p("[-] ERROR: reading .csv : " + str(e), "red")
        exit(1)
    return data_r





def save_csv_dict(file_name, data_dict):
    data = []

    for key,value in data_dict.items():
        tmp = [key]
        tmp.extend(value)
        data.append(tmp)

    try:
        with open(file_name, "w") as f:
            writer = csv.writer(f)
            writer.writerows(data)
        color.p("[+] SUCCESS: saving " + file_name, "gre")
    except Exception as e:
        color.p("[-] ERROR: saving .csv : " + str(e), "red")
