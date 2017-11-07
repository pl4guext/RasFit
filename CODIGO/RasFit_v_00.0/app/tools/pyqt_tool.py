#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from PyQt5.QtCore import QCoreApplication



class Window(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        QToolTip.setFont(QFont('SansSerif', 10))
        
        self.setToolTip('This is a <b>QWidget</b> widget')
        
 

        self.btn2 = QPushButton('Dialog', self)
        self.btn2.move(20, 20)
        self.btn2.clicked.connect(self.showDialog)  

        self.le = QLineEdit(self)
        self.le.move(130, 20) 

        btn = QPushButton('Quit', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.clicked.connect(QCoreApplication.instance().quit)
        btn.resize(btn.sizeHint())
        btn.move(20, 50)   



        self.sex_btn = QPushButton('Hombre', self)
        self.sex_btn.setCheckable(True)
        self.sex_btn.move(20, 80)

        self.sex_btn.clicked[bool].connect(self.check_sex)
  
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')    
        self.show()

    def closeEvent(self, event):
        
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore() 

    def check_sex(self, pressed):
        print("STATE: "+str(pressed))

        if pressed:
            self.sex_btn.setText("Mujer")
        else:
            self.sex_btn.setText("Hombre")


        


    def showDialog(self):
        
        text, ok = QInputDialog.getText(self, 'Input Dialog', 
            'Enter your name:')
        
        if ok:
            self.le.setText(str(text))