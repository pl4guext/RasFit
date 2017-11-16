#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
from time import sleep
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from PyQt5.QtCore import *


try:
    from app.utils import file_manager, color
    from app.tools import wod_tool
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
        self.create_Main()

    def create_Main(self):

        self.setWindowTitle("RasFit")
        self.setGeometry(50,50,conf.window_size[0], conf.window_size[1] )

        layout = QVBoxLayout(self)
        

        oTabWidget = QTabWidget(self)
        layout.addWidget(oTabWidget)

        oPage1 = Window_SelectUser()
        oPage1.setGeometry(0,0,conf.window_size[0], conf.window_size[1])
        # oLabel1 = QLabel("Hello",self) 
        # oVBox1 = QVBoxLayout() 
        # oVBox1.addWidget(oLabel1)      
        # oPage1.setLayout(oVBox1)

        oPage2 = Window_WOD()
        oPage2.setGeometry(0,0,conf.window_size[0], conf.window_size[1])

        oPage3 = QWidget()
        oPage3.setGeometry(0,0,conf.window_size[0], conf.window_size[1])              

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



    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self) 

        br = QBrush(QColor(0,150,30))   # ( R, G, B)
        qp.setBrush(br)             
        qp.drawRect(7, 7, conf.window_size[0]-40, 55 )  #  ( x1, y1, x2, y2)      

        br = QBrush(QColor(110,200,110))   # ( R, G, B)
        qp.setBrush(br)             
        qp.drawRect(7, 60, conf.window_size[0]-40, conf.window_size[1]-125 )  #  ( x1, y1, x2, y2)  

        qp.end()

    def SelectUser(self, user_list):

        self.combo_users = QComboBox(self)
        self.combo_users.addItems(user_list)
        self.combo_users.move(20, 20) 

        self.btn_sel = QPushButton('Select', self)
        self.btn_sel.move(150, 20)
        self.btn_sel.clicked.connect(self.selUser)  

        text_name = QLabel("Nombre",self)
        text_name.move(20, 70) 
        self.in_name = QLineEdit(self)
        self.in_name.move(150, 70) 

        text_age = QLabel("Edad",self)
        text_age.move(20, 110)
        self.in_age = QLineEdit(self)
        self.in_age.move(150, 110) 

        text_height = QLabel("Altura",self)
        text_height.move(20, 150)
        self.in_height = QLineEdit(self)
        self.in_height.move(150, 150) 

        text_weigth= QLabel("Peso",self)
        text_weigth.move(20, 190)
        self.in_weigth = QLineEdit(self)
        self.in_weigth.move(150, 190) 

        self.sex = "hombre"
        self.btn_sex = QPushButton('Hombre', self)
        self.btn_sex.setCheckable(True)
        self.btn_sex.move(20, 230)
        self.btn_sex.clicked[bool].connect(self.check_sex)

        self.btn_add = QPushButton('Create', self)
        self.btn_add.move(20, 230)
        self.btn_add.clicked.connect(self.addUser)  

        # self.setGeometry(300, 300, 300, 200)
        # self.setWindowTitle('Select User')    
        # self.show()

    def selUser(self):
        global conf
        user_sel = self.combo_users.currentText()
        conf.var_entorno["user_name"] = user_sel
        conf.update_info()
        color.p("[+] SUCCESS: User selected -> " + user_sel, "gre") 


    def addUser(self):
        global conf
        name = self.in_name.text()
        age = self.in_age.text()
        weigth = self.in_weigth.text()
        height = self.in_height.text()

        color.p("[*] INFO: Creating User -> " + name + " (" + self.sex + ")", "blu")

        if name in conf.users:
            color.p("[-] ERROR: User name already exists ", "red")
        else:
            conf.create_user(name, self.sex, int(age), int(weigth), int(height) )
            self.combo_users.addItem(name)


    def check_sex(self, pressed):
        print("STATE: "+str(pressed))

        if pressed:
            self.btn_sex.setText("Mujer")
            self.sex = "mujer"
        else:
            self.btn_sex.setText("Hombre")
            self.sex = "hombre"



class Window_WOD(QWidget):

    def __init__(self):
        super().__init__()
        self.WOD_tool = wod_tool.WOD_Generator()
        
        self.WOD()
        self.timer = QTimer()
        self.time = QTime(0, 0, 0)
        self.timer.timeout.connect(self.timerEvent)
        self.title_color = QBrush(QColor(0,150,30)) 
        self.back_color = QBrush(QColor(110,200,110))



    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self) 

        # br = QBrush(QColor(0,150,30))   # ( R, G, B)
        qp.setBrush(self.title_color)             
        qp.drawRect(7, 7, conf.window_size[0]-40, 55 )  #  ( x1, y1, x2, y2)      

        # br = QBrush(QColor(110,200,110))   # ( R, G, B)
        qp.setBrush(self.back_color)             
        qp.drawRect(7, 60, conf.window_size[0]-40, conf.window_size[1]-125 )  #  ( x1, y1, x2, y2)  

        br = QBrush(QColor(255,255,255))   # ( R, G, B)
        qp.setBrush(br)             
        qp.drawRect(140, 260, 195, 48 )  #  ( x1, y1, x2, y2) 

        qp.end()

    def timerEvent(self):
        self.time = self.time.addMSecs(10)
        minutes = self.time.minute()
        secs = self.time.second()
        msecs = self.time.msec()

        total = minutes*60 + secs 
        str_time = str(minutes).zfill(2) + ":" + str(secs).zfill(2) + ":" + str(msecs)[:2].zfill(2) 
        self.update_timer(total, str_time)

       


    def update_timer(self, total_time, string_time):

        if total_time >= 3 :
            self.timer.stop()
            self.time = QTime(0, 0, 0)
            self.title_color = QBrush(QColor(150,30,0)) 
            self.back_color = QBrush(QColor(200,110,110))
            self.repaint()
            self.WOD_tool.save_results([1,2,3], conf)


        self.text_timer.setText(string_time)


    def WOD(self):
        self.combo_WODs = QComboBox(self)
        self.combo_WODs.addItems(self.WOD_tool.WOD_types)
        self.combo_WODs.move(20, 20) 

        self.btn_sel = QPushButton('Generate', self)
        self.btn_sel.move(150, 20)
        self.btn_sel.clicked.connect(self.generate_WOD) 

        self.cb_bands = QCheckBox('Bandas Elasticas', self)
        # self.cb_bands.setCheck
        self.cb_bands.move(20, 60) 
        self.cb_dumbels = QCheckBox('Pesas', self)
        self.cb_dumbels.move(20, 100) 
        self.cb_heavy_dumbels = QCheckBox('Lastres', self)
        self.cb_heavy_dumbels.move(20, 140) 
        self.cb_rings = QCheckBox('Anillas', self)
        self.cb_rings.move(20, 180) 
        self.cb_bar = QCheckBox('Barra Dominadas', self)
        self.cb_bar.move(20, 220) 


        self.btn_sel = QPushButton('Start', self)
        self.btn_sel.move(30, 270)
        self.btn_sel.clicked.connect(self.start_WOD) 

        self.text_timer = QLabel("00:00:00",self)
        self.text_timer.setStyleSheet("font: 30pt Comic Sans MS")
        self.text_timer.move(150, 260)  


    def generate_WOD(self):
        conf.var_entorno["wod_type"] = self.combo_WODs.currentText()
        self.check_material()

        self.WOD_tool.get_random_WOD(conf.var_entorno["wod_type"], conf.all_exercises, conf.user_history)
        
        color.p("[*] INFO: WOD Generated ", "blu")

    def start_WOD(self):

        color.p("[*] INFO: Starting WOD ", "blu")
        self.timer.start(10)  #llama a la funcion timer cada X ms


    def check_material(self):
        if self.cb_bands.isChecked():
            self.WOD_tool.material["bands"]=True
        else:
            self.WOD_tool.material["bands"]=False

        if self.cb_dumbels.isChecked():
            self.WOD_tool.material["dumbels"]=True
        else:
            self.WOD_tool.material["dumbels"]=False

        if self.cb_heavy_dumbels.isChecked():
            self.WOD_tool.material["heavy_dumbels"]=True
        else:
            self.WOD_tool.material["heavy_dumbels"]=False

        if self.cb_rings.isChecked():
            self.WOD_tool.material["rings"]=True
        else:
            self.WOD_tool.material["rings"]=False

        if self.cb_bar.isChecked():
            self.WOD_tool.material["bar"]=True
        else:
            self.WOD_tool.material["bar"]=False

    







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
