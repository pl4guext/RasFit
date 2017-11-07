#!/usr/bin/python3
# -*- coding: utf-8 -*-



try:
    from app.utils import color
except Exception as e:
    print('FAILED TO IMPORT INNER TOOLS in main_menu.py: '+str(e))
    exit(1)


####################### INIT ########################
#####################################################
# def init(conf):

#////////////////////////////////////////////////////




#################### METODOS ########################
#####################################################

#////////////////////////////////////////////////////


#################### MAIN ###########################
#####################################################
def main_menu(conf):
    # conf.create_user("name3", "sex3", 3, 3, 3)
    # conf.delete_user("name3")

    print(conf.users)
