#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget

try:
    from app.tools import pyqt_tool
    from app.main_menu import main_menu
    from config import *
except Exception as e:
    print('ERROR IMPORTING INNER TOOLS from run.py: '+str(e))
    exit(1)






if __name__ == "__main__":

    conf = environment_variables()

    app = QApplication(sys.argv)

    root = pyqt_tool.MainWindow(conf) 
    
    sys.exit(app.exec_())


    # main_menu(conf,root)





        
 


