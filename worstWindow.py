# importing tkinter module
import pickle
from tkinter import *

filename = 'betalinger.pk'

class worstWindowClass:
    def __init__(self, master):
        self.master = master #reference til main window objektet
        self.worstWindow = Toplevel(self.master.root)
        self.worstWindow.title("Bottom 3")
        self.worstWindow.geometry("200x200")
        self.fodboldtur = {}
        from operator import itemgetter
        #Sidsteplads = sorted(fodboldtur.items(), key=itemgetter(1))
        #Label(self.worstWindow, text="De værste betalere").pack()

infile = open(filename,'rb')
fodboldtur = pickle.load(infile)
infile.close()