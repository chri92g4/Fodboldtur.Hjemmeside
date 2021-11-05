# importing tkinter module
from tkinter import *
from tkinter import messagebox
import pickle

filename = 'betalinger.pk'


class payWindowClass:

    def __init__(self, master):

        self.fodboldtur = {}
        infile = open(filename, 'rb')
        self.fodboldtur = pickle.load(infile)
        infile.close()



        self.master = master #reference til main window objektet
        self.payWindow = Toplevel(self.master.root)
        self.payWindow.title("Pay Window")
        self.payWindow.geometry("300x500")

        Label(self.payWindow,
              text="Hvem skal betale").pack()

        self.money = Entry(self.payWindow)
        self.money.pack()

        self.button = Button(self.payWindow, text="betal", command= self.addMoney)
        self.button.pack()

    def addMoney(self):
        try:
            amount = (int(self.money.get())) #HUSK AT VALIDERE INPUT!, kun positive heltal!
        except:
            messagebox.showerror(parent=self.payWindow , title="Beløb fejl!", message="Prøv igen.\nKun hele tal!")
            return

        self.master.total += amount
        self.master.progressLabelText.set(f"Indsamlet: {self.master.total} af {self.master.target} kroner:")
        print(f"Indsamlet: {self.master.total} af {self.master.target} kroner!")
        self.master.progress['value'] = self.master.total / self.master.target * 100


infile = open(filename,'rb')
fodboldtur = pickle.load(infile)
infile.close()