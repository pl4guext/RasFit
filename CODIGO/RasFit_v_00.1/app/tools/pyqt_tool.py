#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from PyQt5.QtCore import QCoreApplication


try:
    from app.utils import file_manager, color
except Exception as e:
    print('ERROR IMPORTING INNER TOOLS from run.py: '+str(e))
    exit(1)



def init_params(configuration):
    global conf
    conf = configuration


class MainWindow(QWidget):

    def __init__(self, config):   
        super().__init__()

        init_params(config)

        self.setWindowTitle("RasFit")
        self.setGeometry(50,50,400,400)

        layout = QVBoxLayout(self)
        

        oTabWidget = QTabWidget(self)
        layout.addWidget(oTabWidget)

        oPage1 = Window_SelectUser()
        # oLabel1 = QLabel("Hello",self) 
        # oVBox1 = QVBoxLayout() 
        # oVBox1.addWidget(oLabel1)      
        # oPage1.setLayout(oVBox1)

        oPage2 = QWidget()
        oPage2.setGeometry(0,0,400,400)

        oPage3 = QWidget()
        oPage3.setGeometry(0,0,400,400)              

        oTabWidget.addTab(oPage1,"Config")
        oTabWidget.addTab(oPage2,"Training")
        oTabWidget.addTab(oPage3,"Stats")      

        self.show()

    
    def closeEvent(self, event):
        
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore() 



class Window_SelectUser(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.SelectUser(conf.users.keys())


    def SelectUser(self, user_list):
        self.combo_users = QComboBox(self)
        self.combo_users.addItems(user_list)
        self.combo_users.move(20, 20) 

        self.btn_sel = QPushButton('Select', self)
        self.btn_sel.move(150, 20)
        self.btn_sel.clicked.connect(self.selUser)  

        text_name = QLabel("Nombre",self)
        text_name.move(20, 60) 
        self.in_name = QLineEdit(self)
        self.in_name.move(150, 60) 

        text_age = QLabel("Edad",self)
        text_age.move(20, 100)
        self.in_age = QLineEdit(self)
        self.in_age.move(150, 100) 

        text_height = QLabel("Altura",self)
        text_height.move(20, 140)
        self.in_height = QLineEdit(self)
        self.in_height.move(150, 140) 

        text_weigth= QLabel("Peso",self)
        text_weigth.move(20, 180)
        self.in_weigth = QLineEdit(self)
        self.in_weigth.move(150, 180) 

        self.sex = "hombre"
        self.btn_sex = QPushButton('Hombre', self)
        self.btn_sex.setCheckable(True)
        self.btn_sex.move(20, 220)
        self.btn_sex.clicked[bool].connect(self.check_sex)

        self.btn_add = QPushButton('Create', self)
        self.btn_add.move(20, 260)
        self.btn_add.clicked.connect(self.addUser)  

        # self.setGeometry(300, 300, 300, 200)
        # self.setWindowTitle('Select User')    
        # self.show()

    def selUser(self):
        user_sel = self.combo_users.currentText()
        print("User " + user_sel + " selected")


    def addUser(self):
        name = self.in_name.text()
        age = self.in_age.text()
        weigth = self.in_weigth.text()
        height = self.in_height.text()

        color.p("- Creating User: " + name + " (" + self.sex + ")", "blu")

        if name in conf.users:
            color.p("[-] ERROR: User name already exists ", "red")
        else:
            conf.create_user(name, self.sex, int(age), int(weigth), int(height) )
            self.combo_users.addItems(name)


    def check_sex(self, pressed):
        print("STATE: "+str(pressed))

        if pressed:
            self.btn_sex.setText("Mujer")
            self.sex = "mujer"
        else:
            self.btn_sex.setText("Hombre")
            self.sex = "hombre"

class Window_NewUser(QWidget):
    
    def __init__(self):
        super().__init__()
        self.NewUser()

    def NewUser(self):
        
        self.btn2 = QPushButton('Dialog', self)
        self.btn2.move(20, 20)
        # self.btn2.clicked.connect(self.showDialog)  

        self.le = QLineEdit(self)
        self.le.move(130, 20) 

        btn = QPushButton('Quit', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.clicked.connect(QCoreApplication.instance().quit)
        btn.resize(btn.sizeHint())
        btn.move(20, 50)   



        # self.sex_btn = QPushButton('Hombre', self)
        # self.sex_btn.setCheckable(True)
        # self.sex_btn.move(20, 80)

        # self.sex_btn.clicked[bool].connect(self.check_sex)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')    
        self.show()



class Window(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.Window_SelectUser()
        
        
    def Open_NewUser(self):
        widget = Window_NewUser()
        widget.exec_()

    def Window_NewUser(self):
        
        QToolTip.setFont(QFont('SansSerif', 10))
        
        self.setToolTip('Add new User')
        


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