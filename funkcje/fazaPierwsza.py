from tkinter import *
from functools import partial
from funkcje.fazaDruga import *

def pierwszyKlik(window,bomby,dane,i,j): #po pierwszym kliknięciu przejdź do fazy drugiej z tymi samymi parametrami
    fazaDruga(window,bomby,dane,i,j)

def fazaPierwsza(window,dane,bomby):
    print(dane)
    s,w = dane #szerokość i wysokość wczytywana z planszy

    elementy = window.place_slaves()
    for l in elementy: #niszczymy poprzenie okno
        l.destroy()
    
    szerokosc = 26*s - 4 #ustalamy szerokość i wysokość każdego pola jako 26 pixeli
    wysokosc = 26*w + 50 #dodatkowe 50 pixeli na menu górne
    window.geometry("{}x{}".format(szerokosc,wysokosc))
         
    frame = Frame(window,bg="#ff0000",width=szerokosc,heigh=wysokosc)
    frame.pack_propagate(0)
    frame.place(x=0,y=0)

    wyswietl = Label(frame,text="Pozostałe bomby do oznaczenia: {}".format(bomby),bg = "#C0C0C0",width = 28,height = 2)
    wyswietl.place(x=40,y=8) #ramka z iloscią bomby-flagi TODO żeby to miało sens

    photo = PhotoImage(file = r"img\retry.png") #dodanie obrazków
    flaga = PhotoImage(file = r"img\flaga.png") 
    bomba = PhotoImage(file = r"img\bomba.png")
    pytajnik = PhotoImage(file = r"img\pytajnik.png")

    reset = Button(frame,bg="#C0C0C0",width=30,heigh=31,image = photo, compound=LEFT) #przycisk resetu
    reset.place(x=3,y=8)

    board = Frame(frame,bg="#808080",width=szerokosc,heigh=int(wysokosc-50))
    board.place(x=0,y=50)

    
  #  bomb = losowanieBomb(bomby)
  #  tab = konwersjaWymiarow(bomb)
   # print(tab)
  #  zlicz(tab)

    tab = [[j%9 for j in range(w)] for i in range(s)]
   # print(tab2)
    for i in range(w):
        for j in range(s):
            bt = Button(board,bg="#C0C0C0",text="    ",command=partial(pierwszyKlik,window,bomby,dane,i,j)) #przyciski
            bt.place(x=j*26,y=i*26) #gdy się wciśnie, to przechodzimy do fazy 2, z znanymi współrzędnymi pierwszego strzału
