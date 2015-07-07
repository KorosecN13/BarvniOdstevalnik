# BarvniOdstevalnik
from tkinter import *
import time

class Odstevalnik():
    
    ''' Elementi odštevalnika '''
    def __init__(self, master):

        self.master = master

        ''' Ozadje'''
        root.configure(background='pink')

        ''' Glavni meni'''
        menu = Menu(master)
        master.config(menu=menu)

        ''' File'''
        file_menu = Menu(menu)
        menu.add_cascade(label="File", menu=file_menu)
        
        ''' Dodamo izbire v file_menu '''
        file_menu.add_command(label="Odpri", command=self.odpri)
        file_menu.add_command(label="Shrani", command=self.shrani)
        file_menu.add_command(label="Izhod", command=master.destroy)
            
        ''' Naredimo spremenljivke, ki hranijo vrednosti polj '''
        self.ime = StringVar(master, value = '')
        self.sekunda = IntVar(master, value = 0)
        self.minuta = IntVar(master, value=0)
        self.ura = IntVar(master, value = 0)

        ''' Oznake'''
        oznaka_ime = Label(master, text = 'ime',)
        oznaka_sekunda = Label(master, text = 's')
        oznaka_minuta = Label(master, text = 'min')
        oznaka_ura = Label(master, text = 'h')

        ''' Gumba'''
        zazeni = Button(master, text = 'ZAŽENI', command = self.zacni_odstevanje, bg='blue')
        ustavi = Button(master, text = 'PRENEHAJ', command = self.ustavi, bg='blue')

        ''' Umestimo jih na glavno okno'''
        oznaka_ime.grid(row = 1, column = 0)
        oznaka_ura.grid(row = 3, column = 3)
        oznaka_minuta.grid(row = 3, column = 5)
        oznaka_sekunda.grid(row = 3, column = 7)
        zazeni.grid(row = 6, column = 9)
        ustavi.grid(row = 6, column = 10)
        
        ''' Kaj moramo povedati programu '''
        polje_ime = Entry(master, width = 10, textvariable = self.ime)
        polje_sekunda = Entry(master, width = 5, textvariable=self.sekunda)
        polje_minuta = Entry(master, width = 5, textvariable=self.minuta)
        polje_ura = Entry(master, width = 5, textvariable=self.ura)

        ''' Umestimo jih na glavno okno'''
        polje_ime.grid(columnspan = 1, row = 1, column = 1) 
        polje_sekunda.grid(row = 3, column = 6)
        polje_minuta.grid(row = 3, column = 4)
        polje_ura.grid(row = 3, column = 2)

        ''' izpis štoparice ure:minute:sekunde ''' 
        self.v = StringVar()
        self.v.set(str(0) + ':' + str(0) + ':' + str(0))
        Label(master, textvariable = self.v).grid(row=5, column=8)

        self.koncni_izpis = Label(master, text = 'Pa je konec! Kaj pa zdaj?')

    def zacni_odstevanje(self):
        root.configure(background='pink')
        self.koncni_izpis.grid_forget()
        self.ostalo = self.ura.get()*3600 + self.minuta.get()*60 + self.sekunda.get() +1
        self.odstevaj()

    def odstevaj(self):
        if self.ostalo != 0:
            while (self.ostalo > 0):
                self.ostalo -= 1
                izpis1 = self.ostalo//3600
                izpis2 = (self.ostalo%3600)//60
                izpis3 = (self.ostalo%3600)%60
                self.v.set(str(izpis1) + ':' + str(izpis2) + ':' + str(izpis3))
                if self.ostalo == 5:
                    self.spremeni_ozadje()
                if self.ostalo == 0:
                    self.koncaj()
                break
            self.master.after(1000, self.odstevaj)            
           
    def spremeni_ozadje(self):
        root.configure(background='red')
            
    def koncaj(self):
        root.configure(background='lightblue')
        self.koncni_izpis.grid(columnspan = 6, row = 6, column = 1)

    def ustavi(self):
        self.v.set('0:0:0')
        self.ostalo = 0

    def odpri(self):
        ime = filedialog.askopenfilename()
        self.v.set('0:0:0')
        self.ostalo = 0
        self.odstevaj()
        sez = []
        numbers = []

        with open(ime) as f:
            for v in f:
                b = v.split(':')
                sez = []
                numbers = []
                for i in b:
                    sez.append(i.strip())
                    for elt in i:
                        if elt in '0123456789':
                            if int(i) not in numbers:
                                numbers.append(int(i))
            self.ime.set(sez[0])
            self.ura.set(numbers[0])
            self.minuta.set(numbers[1])
            self.sekunda.set(numbers[2])
  
    def shrani(self):
        ime = filedialog.asksaveasfilename()
        podatki = self.ime.get()+':     '+str(self.ura.get())+':'+str(self.minuta.get()) + ':' +str(self.sekunda.get())
        with open(ime, 'wt', encoding='utf8') as f:
            f.write(podatki)
                 
root = Tk()
root.title('Barvni odštevalnik')
aplikacija = Odstevalnik(root)
root.mainloop()
