#!/usr/bin/python3
# -*- coding: utf-8 -*-



        # self.var_entorno= { "user_name": "default",
        #                     "wod_type": "AMRAP",
        #                     "training_time": 30}



class WOD_Generator:

    def __init__(self):
        self.WOD_types = ["EMOM", "AMRAP", "TIME", "REPS"]
        self.material = { "bands": True, "dumbels": True, "heavy_dumbels":False, "rings":True, "bar":True}


    def get_random_WOD(self, conf):

        

        if conf.var_entorno[wod_type] == "AMRAP":

        elif conf.var_entorno[wod_type] == "EMOM":

        elif conf.var_entorno[wod_type] == "TIME":

        elif conf.var_entorno[wod_type] == "REPS":

        elif conf.var_entorno[wod_type] == "AMRAP":
        print(history)


    def get_proper_exercises(self):

        history = conf.get_user_history()
        parsed_history = {}

        for key, value in history.items():
            if value[]

