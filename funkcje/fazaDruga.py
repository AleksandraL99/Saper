from random import sample
from klasy.Pole import *
from funkcje.gra import *



def losowanieBomb(bomby,s,w,a,b): #funckja losująca bomby
    i = a*s+b
    pola = list(range(0,i))+list(range(i+1,s*w))
    bomb = sample(pola, bomby)

    tab = [[Pole() for col in range(s)] for row in range(w)]
    for i in bomb: #przełożenie z numeru pól nas tablice dwuwymiarową, wpisanie w tych miejsc 1
        xa = i//s
        xb = i%s
        tab[xa][xb].setWartosc(9)


    return tab


def przelicz(tab,s,w):
    for a in range (w):
        for b in range (s):
            i=0
            if tab[a][b].getWartosc() == 9:
                pass
            else:
                if b != s-1 and tab[a][b+1].getWartosc()  == 9:
                    i = i+1
                if b != 0 and tab[a][b-1].getWartosc() == 9:
                    i = i+1
                if a != s-1 and tab[a+1][b].getWartosc() == 9:
                    i = i+1
                if a != 0 and tab[a-1][b].getWartosc() == 9:
                    i = i+1
                if a != w-1 and b != s-1 and tab[a+1][b+1].getWartosc() == 9:
                    i = i+1
                if a != w-1 and b != 0 and tab[a+1][b-1].getWartosc() == 9:
                    i = i+1
                if a != 0 and b != s-1 and tab[a-1][b+1].getWartosc() == 9:
                    i = i+1
                if a !=0 and b != 0 and tab[a-1][b-1].getWartosc() == 9:
                    i = i+1

                tab[a][b].setWartosc(i)

def fazaDruga(window,bomby,dane,i,j):
    s,w = dane
    bomb = losowanieBomb(10,s,w,i,j)#zmienić 5 na bomby
    przelicz(bomb,s,w)
    
   # bomb[i][j].setStan(1)

    odslon=[]
    odsloniecia(bomb,s,w,i,j,odslon)
    print(odslon)
    for i in bomb:
        for j in i:

            print(j.getWartosc(),end="")
     #   print(i)
        print()
        pass
    print()
    for i in bomb:
        for j in i:

            print(j.getStan(),end="")
     #   print(i)
        print()
        pass
    generujPola(window,bomb,s,w)
  #  zlicz(tab)




  #  tab = konwersjaWymiarow(bomb)
   # print(tab)
  #  zlicz(tab)
