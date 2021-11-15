# importing tkinter module
from tkinter import *
from PIL import ImageTk,Image #image stuff - install package: Pillow
import tkinter as Tkinter
import random

class listWindowClass:
    def __init__(self, master):
        self.master = master #reference til main window objektet
        self.listWindow = Toplevel(self.master.root)


        self.table_values = Tkinter.LabelFrame(self.listWindow, text="Liste", borderwidth=10, relief=Tkinter.GROOVE, padx=10,
                                               pady=10)
        self.table_values.grid(row=1, column=0, padx=20, pady=20)

        for i in range(len(self.master.fodboldtur.keys())):  # Rows
            for j in range(2):  # Columns
                b = Tkinter.Label(self.table_values,bd=10,relief="solid", text="", width=15)
                b.grid(row=i, column=j)

                if j == 0: #så ved vi at vi er i første søjle og det er Str(keys.navne)
                    b.config(text=list(self.master.fodboldtur.keys())[i])

                else:
                    b.config(text=str(self.master.fodboldtur[list(self.master.fodboldtur.keys())[i]]))



    def dataReadout(self, frame):
        # returns Dict of row and column
        pass
