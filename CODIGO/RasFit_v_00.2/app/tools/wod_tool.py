#!/usr/bin/python3
# -*- coding: utf-8 -*-

import datetime
from random import randint


        # self.var_entorno= { "user_name": "default",
        #                     "wod_type": "AMRAP",
        #                     "training_time": 30}



class WOD_Generator:

    def __init__(self):
        self.WOD_types = ["EMOM", "AMRAP", "TIME", "REPS"]
        self.material = { "bands": True, "dumbels": True, "heavy_dumbels":False, "rings":True, "bar":True}
        self.muscles = [ "pectoral", "cuadriceps", "isquios", "gluteo", "dorsal", "espalda_media", "lumbares", "trapecio", "triceps", "biceps", "hombro", "recto_abdominal", "transverso", "oblicuos"]

        # Parametros de generacion de WODs
        self.days_since = 3 # Dias que deben pasar para que un ejercicio vuelva a repetirse
        self.WOD_time = 30 # Minutos que durará el WOD
        self.WOD_total_exercises = 4 # Ejercicios diferentes dentro de un WOD


    def get_random_WOD(self, wod_selected, exercises, history):

        self.set_proper_exercises(exercises, history)

        actual_WOD = self.generate_ARMRAP()
  
        # if conf.var_entorno[wod_type] == "AMRAP":

        # elif conf.var_entorno[wod_type] == "EMOM":

        # elif conf.var_entorno[wod_type] == "TIME":

        # elif conf.var_entorno[wod_type] == "REPS":

        print(actual_WOD)


    def set_proper_exercises(self, all_exercises, user_history):

        self.proper_exercises = {}
        
        for key, value in all_exercises.items():#  exercise_name:  [ tipo, dificultad, musculo, material ]
            if int(user_history[key][1]) > self.days_since : # exercise_name:  [ date, days_since, reps ]
                if value[3]!="n/a":
                    if self.material[value[3]]:
                        self.proper_exercises[key] = value
                else:
                    self.proper_exercises[key] = value
                


    def save_results(self, results, conf):

        conf.save_user_level(results)



    def generate_ARMRAP(self):
        generated_WOD = [ [], [], [], [] ] #  [ [names], [tipos], [dificultades], [musculo] ]
        list_exercises = list(self.proper_exercises.keys() )
        num_exer = len(list_exercises)-1

        while len(generated_WOD[0] ) < self.WOD_total_exercises :
            tmp_rand = randint(0, num_exer)
            if list_exercises[tmp_rand] not in generated_WOD[0]:
                # if  
                generated_WOD[0].append(list_exercises[tmp_rand])
                generated_WOD[1].append(self.proper_exercises[list_exercises[tmp_rand]][0]) #exercise_name:  [ tipo, dificultad, musculo, material ]
                generated_WOD[2].append(self.proper_exercises[list_exercises[tmp_rand]][1])
                generated_WOD[3].append(self.proper_exercises[list_exercises[tmp_rand]][2])

        return generated_WOD
            
