#!/usr/bin/python3
# -*- coding: utf-8 -*-


from Tkinter import *



class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)               
        self.master = master
        self.wod_select = IntVar()
        self.wod_select.set(0)
        self.user_name = Entry(self)
        self.age = Entry(self)
        self.sex = IntVar()
        self.New_User()


    #Creation of init_window
    def Main_menu(self):

        # changing the title of our master widget      
        self.master.title("Menu Principal")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        wod_types= [ "for_time", "for_reps", "for_rounds"]

        Label(self, 
            text="Elige tipo de WOD:",
            justify = LEFT,
            padx = 20).pack()
        for index, wod in enumerate(wod_types): 
            Radiobutton(self, 
                        text=wod,
                        padx = 20, 
                        variable=self.wod_select,
                        command=self.ShowChoice, 
                        value=index).pack(anchor=W)

        
    def New_User(self):
            # changing the title of our master widget      
        self.master.title("Nuevo Usuario")

        # allowing the widget to take the full space of the root window
        self.pack(side=TOP, fill=X, padx=5, pady=5)

        Label(self, text="Nombre",anchor='w').grid(row=0)
        Label(self, text="Edad",anchor='w').grid(row=1)

        
        self.user_name.grid(row=0, column=1)
        self.age.grid(row=1, column=1)

        Label(self, text="Sexo",anchor='w').grid(row=2)
        Radiobutton(self,text="Hombre",padx = 20,variable=self.sex, command=self.ShowChoice, value=0).grid(row=2,column=1)
        Radiobutton(self,text="Mujer",padx = 20,variable=self.sex, command=self.ShowChoice, value=1).grid(row=2,column=2)


        Button(self, text='Cancel', command=self.client_exit).grid(row=4, column=0, sticky=W, pady=4)
        Button(self, text='Save', command=self.add_user).grid(row=4, column=1, sticky=W, pady=4)



        # quitButton = Button(self, text="Cancel", command=self.client_exit)
        # quitButton.place(x=0, y=0)
        


#    for field in fields:
#       row = Frame(root)
#       lab = Label(row, width=15, text=field, anchor='w')
#       ent = Entry(row)
#       row.pack(side=TOP, fill=X, padx=5, pady=5)
#       lab.pack(side=LEFT)
#       ent.pack(side=RIGHT, expand=YES, fill=X)
#       entries.append((field, ent))



    def client_exit(self):
        exit()
    
    def add_user(self):

        print("saved!!!!!!!!")

    def ShowChoice(self):
        print(self.wod_select.get())


