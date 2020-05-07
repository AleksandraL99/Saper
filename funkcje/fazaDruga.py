from random import sample
from klasy.Pole import *
from funkcje.gra import *

def losowanieBomb(bomby,s,w,a,b): #funckja losująca bomby, przyjmuje takie argumenty jak ilość bomb, szerokość i wysokość planszy oraz współrzędne pierwszego strzału
    i = a*s+b #ustalenie numeru pola w które strzelił gracz
    pola = list(range(0,i))+list(range(i+1,s*w))
    bomb = sample(pola, bomby) #losowanie bomb śrób pozostałych pól

    tab = [[Pole() for col in range(s)] for row in range(w)]
    for i in bomb: #przełożenie z numeru pól nas tablice dwuwymiarową
        xa = i//s
        xb = i%s
        tab[xa][xb].setWartosc(9) #ustawienie wartości 9 w miejscach pól z bombami
    return tab #zwraca tablicę z oznaczonymi polami bomb

def przelicz(tab,s,w): #funkcja przeliczająca numery pojawiające się w danym polu
    for a in range (w):
        for b in range (s):
            i=0 #licznik do liczenia bomb w sąsiedztwie
            if tab[a][b].getWartosc() == 9: #nie przelicza jeśli już ma wartość 9
                pass
            else:
                if b != s-1 and tab[a][b+1].getWartosc()  == 9: #na prawo
                    i = i+1
                if b != 0 and tab[a][b-1].getWartosc() == 9: #na lewo
                    i = i+1
                if a != w-1 and tab[a+1][b].getWartosc() == 9: #dół
                    i = i+1
                if a != 0 and tab[a-1][b].getWartosc() == 9: #góra
                    i = i+1
                if a != w-1 and b != s-1 and tab[a+1][b+1].getWartosc() == 9: #prawy dolny róg
                    i = i+1
                if a != w-1 and b != 0 and tab[a+1][b-1].getWartosc() == 9: #lewy doly róg
                    i = i+1
                if a != 0 and b != s-1 and tab[a-1][b+1].getWartosc() == 9: #prawy górny róg
                    i = i+1
                if a !=0 and b != 0 and tab[a-1][b-1].getWartosc() == 9: #lewy dolny róg
                    i = i+1

                tab[a][b].setWartosc(i) #ustawiamy taką wartość, jaką obliczyliśmy

def fazaDruga(window,bomby,dane,i,j):
    s,w = dane
    bomb = losowanieBomb(bomby,s,w,i,j) # TODO zmienić 10 na bomby, dlaczego wyrzuca błąd?
    przelicz(bomb,s,w) #nadanie wartości w tablicy 
    
   # bomb[i][j].setStan(1)
    odslon=[] #tworzymy pustą tablice odsłonięć
    odsloniecia(bomb,s,w,i,j,odslon)
  #  print(odslon) #kontrolne wypisywanie 
    for i in bomb:
        for j in i:
            print(j.getWartosc(),end=" ")
        print()
    print()
    for i in bomb:
        for j in i:
            print(j.getStan(),end="")
        print()

    generujPola(window,bomb,s,w,bomby) #przechodzimy do gry właściwej