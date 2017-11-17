#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, os


try:
    from app.utils import file_manager
    from app.utils import color
    from app.tools import other_tool
except Exception as e:
    print('FAILED TO IMPORT INNER TOOLS from config.py: ' +str(e))
    exit(1)




class environment_variables:

    def __init__(self):

        self.base_dir = sys.path[0]
        self.exercises_path = os.path.join(self.base_dir,"app/data/exercises/")
        self.users_path = os.path.join(self.base_dir,"app/data/user_data/")
        self.users_file = self.users_path + "users.csv"
        self.today = other_tool.today()
        self.var_entorno= { "user_name": "pablo",
                            "wod_type": "AMRAP",
                            "training_time": 3}
        self.update_info()

        #SIZES
        self.window_size = [400, 400] # [ Width, Height ]
        


    def update_info(self):
        self.users = file_manager.read_csv_dict(self.users_file) # users:  [ name, sex, age, weigth, height, IMC]
        self.set_user_params()
        self.update_history()
        

    def set_user_params(self):
        self.user_levels = file_manager.read_csv_dict(self.users_path + self.var_entorno["user_name"] + "_level.csv") # date: [ dominadas, flexiones, pistol_squats ]
        dates = list(self.user_levels.keys())
        diffs = []
        for date in dates:
            diffs.append(other_tool.calculate_days(date))

        min_diff = min(diffs)

        self.actual_level = self.user_levels[ dates[diffs.index(min_diff)]] 
        self.user_history = file_manager.read_csv_dict(self.users_path + self.var_entorno["user_name"] + "_history.csv") #  # exercise_name:  [ date, days_since, reps ]
        self.all_exercises = file_manager.read_csv_dict(self.exercises_path  + "exercises.csv") #  exercise_name:  [ tipo, dificultad, musculo, material ]

    def update_history(self):
        for key, value in self.user_history.items():
            self.user_history[key][1] = other_tool.calculate_days(value[0])
            
        file_manager.save_csv_dict(self.users_path + self.var_entorno["user_name"] + "_history.csv",  self.user_history)
        

            

    def create_user(self, name, sex, age, weigth, height):
        actual_users = self.users
        if name not in actual_users:

            IMC = other_tool.calc_IMC(weigth, height)
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
  

    def save_user_history(self):
        print("hello")



    def save_user_level(self, actual_level):
        self.user_levels[ self.today ] = actual_level

        file_manager.save_csv_dict(self.users_path + self.var_entorno["user_name"] + "_level.csv", self.user_levels)

        color.p("[+] SUCCESS: Level of user "+ self.var_entorno["user_name"] +" saved", "gre")






