import funkcje.ladujMenu as test
from tkinter import *
from functools import partial
from tkinter.font import *
from klasy.Pole import *

def reset(window):
    elementy = window.place_slaves()
    for l in elementy:
        l.destroy()
    test.ladujMenu(window)
   # print(Pole.getStan())

def fazaTrzecia(window, s, w, status):

    szerokosc = 26*s - 4 
    wysokosc = 26*w + 50 
    window.geometry("{}x{}".format(szerokosc,wysokosc)) #tworzymy okno z startowym menu
    window.title( "Saper" ) #z tytułem saper
    height = window.winfo_screenheight() 
    width = window.winfo_screenwidth() 
    pozycja1=szerokosc/2-85
    pozycja2= wysokosc/6
    
    print("\n width x height = %d x %d (in pixels)\n" %(width, height)) #zczytujemy rozmiar ekranu (możliwa opcja późniejszego dopasowania okna)

    menu = Frame(window,bg="#808080",width=width,heigh=height)
    menu.pack_propagate(0)
    menu.place(x=0,y=0)

    if status == 1:
        label = Label(menu,text="Wygrałeś",bg="#C0C0C0",width=10,font = ("Calibri",25))
        label.place(x=pozycja1,y=pozycja2)
    else:
        label = Label(menu,text="Przegrałeś",bg="#C0C0C0",width=10,font = ("Calibri",25))
        label.place(x=pozycja1,y=pozycja2)

    bt = Button(menu,bg="#C0C0C0",heigh=1, text="Zagraj ponownie",command = lambda:  reset(window))
    bt.place(x=szerokosc/2-45,y=7*wysokosc/10) 

    bt = Button(menu,bg="#C0C0C0",width=10,heigh=1, text="Zakończ grę",command = lambda: window.destroy())
    bt.place(x=szerokosc/2-35,y=4*wysokosc/5) 