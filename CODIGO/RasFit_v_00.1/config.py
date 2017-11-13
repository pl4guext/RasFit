#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, os


try:
    from app.utils import file_manager
    from app.utils import color
    from app.tools import health_tool
except Exception as e:
    print('FAILED TO IMPORT INNER TOOLS from config.py: ' +str(e))
    exit(1)




class environment_variables:

    def __init__(self):

        self.base_dir = sys.path[0]
        self.exercises_path = os.path.join(self.base_dir,"app/data/exercises/")
        self.users_path = os.path.join(self.base_dir,"app/data/user_data/")
        self.users_file = self.users_path + "users.csv"
        self.var_entorno= { "user_name": "default"}
        self.update_info()
        





    def update_info(self):
        self.users = file_manager.read_csv_dict(self.users_file) # users:  [ name, sex, age, weigth, height, IMC]
        


    def create_user(self, name, sex, age, weigth, height):
        actual_users = self.users
        if name not in actual_users:

            IMC = health_tool.calc_IMC(weigth, height)
            new_user = [sex, age, weigth, height, IMC]
            actual_users[name] = new_user

            file_manager.save_csv_dict(self.users_file, actual_users)
            self.update_info()
            color.p("[+] SUCCESS: Usuario "+name+" creado con exito", "gre")

        else:
            color.p("[-] ERROR: Ya existe un usuario con ese nombre", "red")




    def delete_user(self, name):
        actual_users = self.users
        if name in actual_users:
            del actual_users[name]

            file_manager.save_csv_dict(self.users_file, actual_users)
            self.update_info()
            color.p("[+] SUCCESS: Usuario "+name+" eliminado con exito", "gre")
        else:
            color.p("[-] ERROR: No existe ningun usuario con ese nombre", "red")
  

