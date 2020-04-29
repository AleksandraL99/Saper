from tkinter import *
from funkcje.fazaPierwsza import *
from klasy.Dane import *

def zmiana_pol_poziom(self,dane,b):

    spix,spiy = dane.getUstawieniaPlanszy()#spix to szerokosc
    spix = int(self.get())
    
    b.config(from_=int(spix*spiy*0.2), to=int(spix*spiy*0.7))

    dane.setUstawieniaPlanszy(spix,spiy)
   

def zmiana_pol_pion(self,dane,b):
    spix,spiy = dane.getUstawieniaPlanszy()
    spiy = int(self.get())

    b.config(from_=int(spix*spiy*0.2), to=int(spix*spiy*0.7))

    dane.setUstawieniaPlanszy(spix,spiy)

def ladujMenu(window):

    dane = Dane()#startowa szerokość planszy
    dane.setUstawieniaPlanszy(10,10)

    window.geometry("{}x{}".format(250,300))
    window.title( "Saper" ) 
    height = window.winfo_screenheight() 
    width = window.winfo_screenwidth() 
  
    print("\n width x height = %d x %d (in pixels)\n" %(width, height)) 

    menu = Frame(window,bg="#808080",width=width,heigh=height)
    menu.pack_propagate(0)
    menu.place(x=0,y=0)

    label = Label(menu,text="Wybierz wielkość pola",bg="#808080",width=30,height=1)
    label.place(x=10,y=20)

    b = Spinbox(menu, from_=20, to=70,state="readonly")
    b.place(x=50,y=150)

    w = Spinbox(menu, from_=10, to=25,state="readonly",command=lambda:zmiana_pol_poziom(w,dane,b))
    w.place(x=50,y=55)
    
    s = Spinbox(menu, from_=10, to=25,state="readonly",command=lambda:zmiana_pol_pion(s,dane,b))
    s.place(x=50,y=80)

    label = Label(menu,text="Wybierz ilość bomb",bg="#808080",width=30,height=1)
    label.place(x=10,y=120)

    bt = Button(menu,bg="#C0C0C0",width=10,heigh=1,command=lambda:fazaPierwsza(window,dane.getUstawieniaPlanszy(),int(b.get())), text="Zatwierdź")
    bt.place(x=75,y=190)
