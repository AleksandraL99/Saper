from tkinter import *
from functools import partial
from funkcje.fazaDruga import *

def pierwszyKlik(window,bomby,dane,i,j):
    fazaDruga(window,bomby,dane,i,j)

def fazaPierwsza(window,dane,bomby):
    print(dane)
    s,w = dane

    elementy = window.place_slaves()
    for l in elementy:
        l.destroy()
    
    szerokosc = 26*s - 4
    wysokosc = 26*w + 50
    window.geometry("{}x{}".format(szerokosc,wysokosc))
         
    frame = Frame(window,bg="#ff0000",width=szerokosc,heigh=wysokosc)
    frame.pack_propagate(0)
    frame.place(x=0,y=0)

    wyswietl = Label(frame,text="Pozostałe bomby do oznaczenia: {}".format(bomby),bg = "#C0C0C0",width = 28,height = 2)
    wyswietl.place(x=40,y=8)

    photo = PhotoImage(file = r"img\retry.png")
    flaga = PhotoImage(file = r"img\flaga.png") 
    bomba = PhotoImage(file = r"img\bomba.png")
    pytajnik = PhotoImage(file = r"img\pytajnik.png")
   # helv36 = tkFont.Font(family='Arial', size=12, weight='bold')

    reset = Button(frame,bg="#C0C0C0",width=30,heigh=31,image = photo, compound=LEFT)
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
            bt = Button(board,bg="#C0C0C0",text="    ",command=partial(pierwszyKlik,window,bomby,dane,i,j))#, font= helv36
        #    bt.bind("<Button-1>", partial(pierwszy,i, j))
         #   bt.bind("<Button-3>", partial(praweKlikniecie,i, j))
            bt.place(x=j*26,y=i*26)





















    for i in range(0):
        for j in range(s):

            if tab[i][j] == 0:
                liczba = " "
                kolor="#C0C0C0"
            elif tab[i][j] == 1:
                liczba = 1
                kolor = "blue"
            elif tab[i][j] == 2:
                liczba = 2
                kolor="green"
            elif tab[i][j] == 3:
                liczba = 3
                kolor = "red"
            elif tab[i][j] == 4:
                liczba = 4
                kolor = "navy"
            elif tab[i][j] == 5:
                liczba = 5
                kolor = "#8B0000"
            elif tab[i][j] == 6:
                liczba = 6
                kolor = "#FFFF00"
            elif tab[i][j] == 7:
                liczba = 7
                kolor = "#DC143C"
            elif tab[i][j] == 8:
                liczba = 8
                kolor = "black"

            bt = Button(board,bg="#C0C0C0",text="{}  ".format(liczba), fg = '{}'.format(kolor))#, font= helv36
            bt.bind("<Button-1>", partial(left,i, j))
            bt.bind("<Button-3>", partial(right,i, j))
            bt.place(x=j*26,y=i*26)
