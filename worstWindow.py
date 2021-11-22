from tkinter import *
from PIL import ImageTk,Image #image stuff - install package: Pillow
import tkinter as Tkinter
import random
from operator import itemgetter  # python importere "itemgetter" fra operator som er den sorterede dict


class worstWindowClass:
    def __init__(self, master):
        self.master = master #reference til main window objektet
        self.listWindow = Toplevel(self.master.root)


        self.table_values = Tkinter.LabelFrame(self.listWindow, text="Liste", borderwidth=10, relief=Tkinter.GROOVE, padx=10,
                                               pady=10)
        self.table_values.grid(row=1, column=0, padx=20, pady=20)


        sidsteplads = sorted(self.master.fodboldtur.items(), key=itemgetter(1))[0:3] #giver "sidsteplads" en defination som jeg kan kalde når det skal printes.
        print(sidsteplads)

        for i in range(len(sidsteplads)):  # Rows
            for j in range(2):  # Columns
                b = Tkinter.Label(self.table_values,bd=10,relief="solid", text="", width=25)
                b.grid(row=i, column=j)

                b.config(text=sidsteplads[i][j])



    def dataReadout(self, frame):
        # returns Dict of row and column
        pass
