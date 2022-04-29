# importing tkinter module
import pickle
from tkinter import *
from tkinter.ttk import * #progressbar

from listWindow import listWindowClass
from payWindow import payWindowClass
from worstWindow import worstWindowClass

filename = 'betalinger.pk'

#john regner, john ser alt
def john():
    pass




class mainWindow:

    def __init__(self):
        self.fodboldtur = {}
        infile = open(filename, 'rb')
        self.fodboldtur = pickle.load(infile)
        infile.close()

        def afslut():  # giver afslut en funktion som man kan køre i koden
            outfile = open(filename, 'wb')  # python åbner filen
            pickle.dump(self.fodboldtur, outfile)  # python gemmer filen
            outfile.close()  # python lukker filen
            print("Programmet er afsluttet!")

        print(self.fodboldtur)
        Sum = 0  # definerer sum som en int
        for key in self.fodboldtur.keys():  # ber programmet om at sætte beløb som en key som jeg kan definerer senere
            Sum += self.fodboldtur[key]  # tilføjer beløbne en efter en og ber programmet tjekke om der er nyt beløb
        print(Sum - 4500,
              "kroner")  # ber programmet printe den fulde sum -4500 så brugeren ved hvor meget der mangler i alt

        self.total = Sum
        self.target = 4500
        self.root = Tk()


        #TEXT

        velkomst = Label(self.root, text="Velkommen til fodboldtur GUI")
        velkomst.pack(pady=10)

        # Progress bar widget
        self.progressLabelText = StringVar()
        self.progressLabelText.set(f"Indsamlet: {self.total} af {self.target} kroner:")

        self.progressLabel = Label(self.root, textvariable=self.progressLabelText)
        self.progressLabel.pack()
        self.progress = Progressbar(self.root, orient = HORIZONTAL,
                    length = 250, mode = 'determinate')
        self.progress['value'] = self.total/self.target*100
        #print(self.progress['length'])
        #print(self.progress['value'])
        #BUTTONS
        self.progress.pack(padx= 20)

        listButton = Button(self.root,text ="Liste over indbetalinger",command = lambda: listWindowClass(self))
        listButton.pack(padx = 20, pady = 10,side=LEFT)


        payButton = Button(self.root,text ="Indbetal",command = lambda: payWindowClass(self))
        payButton.pack(padx = 20, pady = 10,side=LEFT)

        bottom3Button = Button(self.root,text ="Bund 3",command = lambda: worstWindowClass(self))
        bottom3Button.pack(padx = 20, pady = 10,side=LEFT)

        # infinite loop
        mainloop()

        afslut()

if __name__ == '__main__':
    main = mainWindow()
