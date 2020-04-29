from klasy.Pole import *
from tkinter import *
from functools import partial

def odsloniecia(tab,s,w,a,b,odslon):
    print(tab[a][b].getWartosc(),tab[a][b].getStan())
    if tab[a][b].getWartosc() == 0 and tab[a][b].getStan() == 0:
        tab[a][b].setStan(1)
        odslon.append((a,b))
        if a != 0:
            odsloniecia(tab,s,w,a-1,b,odslon)
        if a != w-1:
            odsloniecia(tab,s,w,a+1,b,odslon)
        if b != 0:
            odsloniecia(tab,s,w,a,b-1,odslon)
        if b != s-1:
            odsloniecia(tab,s,w,a,b+1,odslon)   
    else:
        tab[a][b].setStan(1)
        odslon.append((a,b))
        if a !=w-1 and b!=0 and tab[a+1][b].getWartosc()==0:
            tab[a][b-1].setStan(1)
            odslon.append((a,b-1))
        if a !=0 and b!=s-1 and tab[a-1][b].getWartosc()==0:
            tab[a][b+1].setStan(1)
            odslon.append((a,b+1))
        #if a != 0 and b!= k-1 and tab[a][b+1]==0:
           # tab2[a-1][b]='o'
           #k to w, n to s

def zmianaPrzyciskow(tab,i,j,bt):
    flaga = PhotoImage(file = r"img\flaga.png") 
    bomba = PhotoImage(file = r"img\bomba.png")
    pytajnik = PhotoImage(file = r"img\pytajnik.png")

    

def leweKlikniecie(tab,i,j,self):
    if tab[i][j].getStan() == 0:
        print(i,j)
    else:
        print("tu jest flaga/znak zapytania, nie da się sttrzelić")

def praweKlikniecie(tab,i,j,bt,self):
    flaga = PhotoImage(file = r"img\flaga.png")
    pytajnik = PhotoImage(file = r"img\pytajnik.png")
   

    if tab[i][j].getStan() == 0:
        tab[i][j].setStan(2)
        logo = flaga.subsample(2, 2)
        bt.config(image = logo)
        bt.image = logo
    elif tab[i][j].getStan() == 2:
        tab[i][j].setStan(3)
        logo = pytajnik.subsample(2, 2)
        bt.config(image = logo )
        bt.image = logo
    elif tab[i][j].getStan() == 3:
        tab[i][j].setStan(0)
        bt.config(image = "")


def generujPola(window,tab,s,w):

    elementy = window.place_slaves()
    for l in elementy:
        l.destroy()

    szerokosc = 26*s - 4
    wysokosc = 26*w + 50
    frame = Frame(window,bg="#ff0000",width=szerokosc,heigh=wysokosc)
    frame.pack_propagate(0)
    frame.place(x=0,y=0)

    wyswietl = Label(frame,text="Pozostałe bomby do oznaczenia: {}".format(1),bg = "#C0C0C0",width = 28,height = 2)
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

    for i in range(w):
        for j in range(s):
            if  tab[i][j].getStan():
                if tab[i][j].getWartosc() == 0:
                    liczba = " "
                    kolor="#C0C0C0"
                elif tab[i][j].getWartosc() == 1:
                    liczba = 1
                    kolor = "blue"
                elif tab[i][j].getWartosc() == 2:
                    liczba = 2
                    kolor="green"
                elif tab[i][j].getWartosc() == 3:
                    liczba = 3
                    kolor = "red"
                elif tab[i][j].getWartosc() == 4:
                    liczba = 4
                    kolor = "navy"
                elif tab[i][j].getWartosc() == 5:
                    liczba = 5
                    kolor = "#8B0000"
                elif tab[i][j].getWartosc() == 6:
                    liczba = 6
                    kolor = "#FFFF00"
                elif tab[i][j].getWartosc() == 7:
                    liczba = 7
                    kolor = "#DC143C"
                elif tab[i][j].getWartosc() == 8:
                    liczba = 8
                    kolor = "black"

                bt = Button(board,bg="#C0C0C0",text="{}  ".format(liczba), fg = '{}'.format(kolor))#, font= helv36
                bt.place(x=j*26,y=i*26)
            else:
                bt = Button(board,bg="#C0C0C0",text="#")#, font= helv36
                bt.bind("<Button-1>", partial(leweKlikniecie,tab,i, j))
                bt.bind("<Button-3>", partial(praweKlikniecie,tab,i, j, bt))
                bt.place(x=j*26,y=i*26)
    