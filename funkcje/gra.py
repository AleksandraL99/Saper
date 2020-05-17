from klasy.Pole import *
from klasy.Dane import *
from tkinter import *
from functools import partial
from funkcje.fazaTrzecia import *
from time import sleep
import funkcje.ladujMenu as test

def zresetuj(window):
    elementy = window.place_slaves()
    for l in elementy:
        l.destroy()
    test.ladujMenu(window)

def odsloniecia(tab,s,w,a,b,odslon): #funkcja odsłaniajaca po kliknięciu
    #print(tab[a][b].getWartosc(),tab[a][b].getStan()) #wyświetlanie w konsoli tablic zapisanych liczb i stanów
    if tab[a][b].getWartosc() == 0 and tab[a][b].getStan() == 0: #jeśli trafi się w pole z wartością 0 i nieodsłoniętą, to idź rekurencyjnie
        tab[a][b].setStan(1) #ustaw stan na odsłonięcie
        odslon.append((a,b)) #odsłoń
        if a != 0: #jeśli to nie jest element w zerowym wierszu
            odsloniecia(tab,s,w,a-1,b,odslon) #to idź rekurencyjnie do góry
        if a != w-1: #jeśli to nie ostatni wiersz
            odsloniecia(tab,s,w,a+1,b,odslon) #to idź do dołu
        if b != 0: #jeśli to nie zerowa kolumna
            odsloniecia(tab,s,w,a,b-1,odslon) #to idź w lewo
        if b != s-1: #jeśli to nie ostatnia kolumna
            odsloniecia(tab,s,w,a,b+1,odslon)   #to idź w prawo
    else: #jeśli trafimy na komórkę z wartością lub już odsłoniętą
        tab[a][b].setStan(1) #zmień stan na odsłonięty 
        odslon.append((a,b)) #odsłoń ją
        if  a!=0 and tab[a-1][b]==0 and tab2[a-1][b]=='n': #jeśli na górze lub dole od liczby jest 0 (czyli na przekątnej od 0), to wróć do rekurencji
            odsloniecia(tab,s,w,a-1,b,odslon) #do sprawdzenia
        if a!=w-1 and tab[a+1][b]==0 and tab2[a+1][b]=='n': 
            odsloniecia(tab,s,w,a+1,b,odslon)
        if a!=0 and b!=s-1 and tab[a][b+1].getWartosc() == 0 and tab[a-1][b].getWartosc() != 0 and tab[a][b+1].getStan() == 1: #lewy górny róg
            tab[a-1][b].setStan(1) #ustaw stan 1
            odslon.append((a-1,b)) #dodaj element do listy odsłoniętych TODO to chyba niepotrzebne, operujemy na stanach
        if a != w-1 and b!=0 and tab[a][b-1].getWartosc() ==0 and tab[a+1][b].getWartosc() != 0 and tab[a][b-1].getStan() == 1: #prawy dolny róg
            tab[a+1][b].setStan(1)
            odslon.append((a+1,b))
        if a!=w-1 and b!=s-1 and tab[a][b+1].getWartosc() == 0 and tab[a+1][b].getWartosc() !=0 and tab[a][b+1].getStan() == 1: #lewy dolny róg
            tab[a+1][b].setStan(1)
            odslon.append((a+1,b))
        if a != 0 and b!=0 and tab[a][b-1].getWartosc() ==0 and tab[a-1][b].getWartosc() != 0 and tab[a][b-1].getStan() == 1: #prawy górny róg
            tab[a-1][b].setStan(1)
            odslon.append((a-1,b))  

def przegrana(window, tab,btTablica,s,w):
    for i in range(w):
        for j in range(s):
            if tab[i][j].getWartosc() == 9:
                lb = Label(btTablica[i][j].master,text="{}  ".format("B"))
                lb.place(x=j*26,y=i*26)
                btTablica[i][j].destroy()
   # sleep(5)
    fazaTrzecia(window, s, w, 0)

def leweKlikniecie(window,tab,s,w,i,j,btTablica,self): #obsługa kliknięcia lewego
    if tab[i][j].getStan() == 0: #jeśli nieodkryty
        if tab[i][j].getWartosc() == 9:
            przegrana(window,tab,btTablica,s,w)
            print("end")
            return
        odslon = []
        odsloniecia(tab,s,w,i,j,odslon)
        for i,j in odslon:
            liczba,kolor = kololowanko(tab[i][j].getWartosc())       
            lb = Label(btTablica[i][j].master, bg="#808080",text="  {}  ".format(liczba),font = ("Calibri",10), fg = '{}'.format(kolor))
            lb.place(x=j*26,y=i*26)
            btTablica[i][j].destroy()
        warunkiZakonczenia(window, s,w,tab)
    else:
        print("tu jest flaga/znak zapytania, nie da się strzelić")

def zmianaPrzyciskow(tab,i,j,bt): #TODO to w sumie chyba do usunięcia, obrazki dodajemy w obsługach kliknięć
    flaga = PhotoImage(file = r"img\flaga.png") 
    bomba = PhotoImage(file = r"img\bomba.png")
    pytajnik = PhotoImage(file = r"img\pytajnik.png")

def praweKlikniecie(window,s,w,tab,i,j,bt,wyswietl,bomby,self): #obsługa prawego kliknięcia
    flaga = PhotoImage(file = r"img\flaga.png") #w tej części możemy użyć flagi i pytajnika
    pytajnik = PhotoImage(file = r"img\pytajnik.png") #TODO warunki zakończenia

    if tab[i][j].getStan() == 0: #jeśli jeszcze nie był klikany
        tab[i][j].setStan(2) #ustaw stan 2, odpowiedzialny za flagę)
        logo = flaga.subsample(2, 2)
        bt.config(image = logo) #stwórz przycisk z obrazkiem plagi
        bt.image = logo
        bomby.setBomby(bomby.getBomby()-1)
    elif tab[i][j].getStan() == 2: #jeśli stanem było 2 (flaga)
        tab[i][j].setStan(3) #ustaw stan 3, czyli pytajnik
        logo = pytajnik.subsample(2, 2)
        bt.config(image = logo ) #stwórz przycisk z pytajnikiem
        bt.image = logo
        bomby.setBomby(bomby.getBomby()+1)
    elif tab[i][j].getStan() == 3: #jeśli stanem było 3 (pytajnik)
        tab[i][j].setStan(0) #wróć do stanu 0
        bt.config(image = "") #przycisk bez obrazka
    warunkiZakonczenia(window, s,w,tab)
    wyswietl['text'] = "Pozostałe bomby do oznaczenia: {}".format(bomby.getBomby())

def warunkiZakonczenia(window, s,w,tab): #TODO dodać warunek, że wszystkie oprócz bomb są odkryte
    i = 0
    j = 0
    k = 0
    m = 0
    n = s*w
    for a in range (w):
        for b in range (s):
            if tab[a][b].getWartosc() == 9: #przeliczamy ilość bomb, można przekazać w parametrze
                i += 1
            if tab[a][b].getStan() == 2: #liczymy ile jest oznaczonych flagą
                k +=1
            if tab[a][b].getWartosc() == 9 and tab[a][b].getStan() == 2: #porównujemy ilość oznaczonych
                j +=1
            if tab[a][b].getStan() == 1: #liczymy ile odsłoniętych
                m +=1
    if i == j == k or m+i == n: #jeśli warunki spełnione to przejdź do okna zamknięcia
        fazaTrzecia(window, s, w, 1)


def kololowanko(wartosc):
    liczba = "  "
    kolor="#C0C0C0"

    if wartosc == 1:
        liczba = 1
        kolor = "blue"
    elif wartosc == 2:
        liczba = 2
        kolor="green"
    elif wartosc == 3:
        liczba = 3
        kolor = "red"
    elif wartosc == 4:
        liczba = 4
        kolor = "navy"
    elif wartosc == 5:
        liczba = 5
        kolor = "#8B0000"
    elif wartosc == 6:
        liczba = 6
        kolor = "#FFFF00"
    elif wartosc == 7:
        liczba = 7
        kolor = "#DC143C"
    elif wartosc == 8:
        liczba = 8
        kolor = "black"

    return(liczba,kolor)

def generujPola(window,tab,s,w,bomby): #generowanie planszy TODO żeby za każdym razem się nie odświeżała?

    elementy = window.place_slaves()
    for l in elementy:
        l.destroy()

    szerokosc = 26*s - 4 #ustalamy szerokość i wysokość każdego pola jako 26 pixeli
    wysokosc = 26*w + 50 #dodatkowe 50 pixeli na menu górne
    frame = Frame(window,bg="#808080",width=szerokosc,heigh=wysokosc) 
    frame.pack_propagate(0)
    frame.place(x=0,y=0)

    wyswietl = Label(frame,text="Pozostałe bomby do oznaczenia: {}".format(bomby),bg = "#C0C0C0",width = 28,height = 2)
    wyswietl.place(x=40,y=8) 

    photo = PhotoImage(file = r"img\retry.png") 
    flaga = PhotoImage(file = r"img\flaga.png") 
    bomba = PhotoImage(file = r"img\bomba.png")
    pytajnik = PhotoImage(file = r"img\pytajnik.png")

    reset = Button(frame,bg="#C0C0C0",width=30,heigh=31,image = photo, compound=LEFT, command = lambda: zresetuj(window)) #przycisk do resetowania gry
    reset.place(x=3,y=8) #TODO naprawić
    logo = photo.subsample(4, 4)
    reset.config(image = logo) #stwórz przycisk z obrazkiem plagi
    reset.image = logo

    board = Frame(frame,bg="#808080",width=szerokosc,heigh=int(wysokosc-50))
    board.place(x=0,y=50)

    btTablica=[]
    liczbaBomb = Dane()
    liczbaBomb.setBomby(bomby)
    for i in range(w):
        temp=[]
        for j in range(s):
            if  tab[i][j].getStan()==1: #jeśli jest stan równy 1 ustawiony, to wyświetlaj liczby
                liczba,kolor = kololowanko(tab[i][j].getWartosc())                
                bt = Label(board,bg="#808080",text="  {}  ".format(liczba),font = ("Calibri",10), fg = '{}'.format(kolor)) #TODO zmienic font

            else:
                bt = Button(board,bg="#C0C0C0",text="     ") #tworzymy pusty przycisk
                bt.bind("<Button-1>", partial(leweKlikniecie,window, tab, s, w, i, j, btTablica)) #obsługa lewego kliknięcia
                bt.bind("<Button-3>", partial(praweKlikniecie,window,s,w,tab,i, j, bt, wyswietl,liczbaBomb)) #obsługa prawego kliknięcia
            
            bt.place(x=j*26,y=i*26)
            temp.append(bt)
        btTablica.append(temp)


    
