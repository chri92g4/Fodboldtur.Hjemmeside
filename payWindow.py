# importing tkinter module
from tkinter import *
from tkinter import messagebox
import pickle

filename = 'betalinger.pk'


class payWindowClass:

    def __init__(self, master):


        self.master = master #reference til main window objektet
        self.payWindow = Toplevel(self.master.root)
        self.payWindow.title("Pay Window")
        self.payWindow.geometry("300x500")

        self.valgtnavn = StringVar(self.payWindow)
        self.valgtnavn.set("Vælg navn")


        Label(self.payWindow,
              text="Hvem skal betale").pack()


        self.money = Entry(self.payWindow)
        self.money.pack()

        self.namesList=list(self.master.fodboldtur.keys())
        self.w = OptionMenu(self.payWindow, self.valgtnavn, *self.namesList )
        self.w.pack()

        self.button = Button(self.payWindow, text="betal", command= self.addMoney)
        self.button.pack()

    def selectname(self):

        if self.money.get() not in self.master.fodboldtur.keys():
                messagebox.showerror(parent=self.payWindow , title="Fejl med navn!", message="Prøv igen.\nTjek venligst navn er korreke!")
        else:
            pass



    def addMoney(self):
        try:
            amount = (int(self.money.get())) #HUSK AT VALIDERE INPUT!, kun positive heltal!
        except:
            messagebox.showerror(parent=self.payWindow , title="Beløb fejl!", message="Prøv igen.\nKun hele tal!")
            return

        if self.valgtnavn.get() == "Vælg navn":
            messagebox.showerror(parent=self.payWindow, title="Navne fejl!", message="Prøv igen.\nVælg venligst et navn i dropdown:))")
            return

        #update dict
        self.master.fodboldtur[self.valgtnavn.get()]+=amount
        print(self.master.fodboldtur)

        #refresh sum


        self.master.total += amount
        self.master.progressLabelText.set(f"Indsamlet: {self.master.total} af {self.master.target} kroner:")
        print(f"Indsamlet: {self.master.total} af {self.master.target} kroner!")
        self.master.progress['value'] = self.master.total / self.master.target * 100

