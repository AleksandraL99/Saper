import tkinter
from functools import partial

from funkcje import faza_trzecia
from funkcje import laduj_menu
from funkcje import stale
from klasy import Dane

ODSLONIETY = 1
NIEODSLONIETY = 0
STAN_FLAGI = 2
STAN_PYTAJNIKA = 3
WYMIAR_OKIENKA = 26
BOMBA = 9
PUSTY = 0


def zresetuj(window):
    elementy = window.place_slaves()
    for l in elementy:
        l.destroy()
    laduj_menu.laduj_menu(window)


# funkcja odsłaniajaca po kliknięciu
def odsloniecia(tab, szerokosc, wysokosc, wsp_1, wsp_2, odslon):
    # jeśli trafi się w pole z wartością 0 (pustą) i nieodsłoniętą, to idź rekurencyjnie
    if tab[wsp_1][wsp_2].wartosc == PUSTY and tab[wsp_1][wsp_2].stan == NIEODSLONIETY:
        tab[wsp_1][wsp_2].set_stan(1)  # ustaw stan na odsłonięcie
        odslon.append((wsp_1, wsp_2))  # odsłoń
        if wsp_1 != 0:  # jeśli to nie jest element w zerowym wierszu
            # to idź rekurencyjnie do góry
            odsloniecia(tab, szerokosc, wysokosc, wsp_1-1, wsp_2, odslon)
        if wsp_1 != wysokosc-1:  # jeśli to nie ostatni wiersz
            # to idź do dołu
            odsloniecia(tab, szerokosc, wysokosc, wsp_1+1, wsp_2, odslon)
        if wsp_2 != 0:  # jeśli to nie zerowa kolumna
            # to idź w lewo
            odsloniecia(tab, szerokosc, wysokosc, wsp_1, wsp_2-1, odslon)
        if wsp_2 != szerokosc-1:  # jeśli to nie ostatnia kolumna
            # to idź w prawo
            odsloniecia(tab, szerokosc, wysokosc, wsp_1, wsp_2+1, odslon)
    else:  # jeśli trafimy na komórkę z wartością lub już odsłoniętą
        tab[wsp_1][wsp_2].set_stan(ODSLONIETY)  # zmień stan na odsłonięty
        odslon.append((wsp_1, wsp_2))  # odsłoń ją
        # lewy górny róg
        if (wsp_1 != 0 and wsp_2 != szerokosc-1 and tab[wsp_1][wsp_2+1].wartosc == PUSTY and
                tab[wsp_1-1][wsp_2].wartosc != PUSTY and tab[wsp_1][wsp_2+1].stan == ODSLONIETY):
            tab[wsp_1-1][wsp_2].set_stan(1)  # ustaw stan 1
            odslon.append((wsp_1-1, wsp_2))
        # prawy dolny róg
        if (wsp_1 != wysokosc-1 and wsp_2 != 0 and tab[wsp_1][wsp_2-1].wartosc == PUSTY and
                tab[wsp_1+1][wsp_2].wartosc != PUSTY and tab[wsp_1][wsp_2-1].stan == ODSLONIETY):
            tab[wsp_1+1][wsp_2].set_stan(ODSLONIETY)
            odslon.append((wsp_1+1, wsp_2))
        # lewy dolny róg
        if (wsp_1 != wysokosc-1 and wsp_2 != szerokosc-1 and
                tab[wsp_1][wsp_2+1].wartosc == PUSTY and
                tab[wsp_1+1][wsp_2].wartosc != PUSTY and tab[wsp_1][wsp_2+1].stan == ODSLONIETY):
            tab[wsp_1+1][wsp_2].set_stan(ODSLONIETY)
            odslon.append((wsp_1+1, wsp_2))
        # prawy górny róg
        if (wsp_1 != 0 and wsp_2 != 0 and tab[wsp_1][wsp_2-1].wartosc == PUSTY and
                tab[wsp_1-1][wsp_2].wartosc != PUSTY and tab[wsp_1][wsp_2-1].stan == ODSLONIETY):
            tab[wsp_1-1][wsp_2].set_stan(ODSLONIETY)
            odslon.append((wsp_1-1, wsp_2))


# obsługa kliknięcia lewego
def lewe_klikniecie(window, tab, szerokosc, wysokosc, wsp_1, wsp_2, btTablica, self):
    if tab[wsp_1][wsp_2].stan == NIEODSLONIETY:  # jeśli nieodkryty
        if tab[wsp_1][wsp_2].wartosc == 9:
            faza_trzecia.faza_trzecia(window, szerokosc, wysokosc, 0)
            print("end")
            return
        odslon = []
        odsloniecia(tab, szerokosc, wysokosc, wsp_1, wsp_2, odslon)
        for i, j in odslon:
            liczba, kolor = kololowanko(tab[i][j].wartosc)
            lb = tkinter.Label(btTablica[i][j].master, bg=stale.SZARY_CIEMNY,
                               text="  {}  ".format(liczba),
                               font=("Calibri", 10), fg='{}'.format(kolor))
            lb.place(x=j*26, y=i*26)
            btTablica[i][j].destroy()
        warunki_zakonczenia(window, szerokosc, wysokosc, tab)
    else:
        print("Tu jest flaga/znak zapytania, nie da się strzelić")


# obsługa prawego kliknięcia
def prawe_klikniecie(window, szerokosc, wysokosc,
                     tab, wsp_1, wsp_2, przycisk, wyswietl, bomby, self):
    # w tej części możemy użyć flagi i pytajnika
    flaga = tkinter.PhotoImage(file='img/flaga.png')
    pytajnik = tkinter.PhotoImage(file='img/pytajnik.png')

    if tab[wsp_1][wsp_2].stan == 0:  # jeśli jeszcze nie był klikany
        tab[wsp_1][wsp_2].set_stan(2)  # ustaw stan 2, odpowiedzialny za flagę)
        logo = flaga.subsample(2, 2)
        przycisk.config(image=logo)  # stwórz przycisk z obrazkiem plagi
        przycisk.image = logo
        bomby.set_bomby(bomby.get_bomby()-1)
    elif tab[wsp_1][wsp_2].stan == 2:  # jeśli stanem było 2 (flaga)
        tab[wsp_1][wsp_2].set_stan(3)  # ustaw stan 3, czyli pytajnik
        logo = pytajnik.subsample(2, 2)
        przycisk.config(image=logo)  # stwórz przycisk z pytajnikiem
        przycisk.image = logo
        bomby.set_bomby(bomby.get_bomby()+1)
    elif tab[wsp_1][wsp_2].stan == 3:  # jeśli stanem było 3 (pytajnik)
        tab[wsp_1][wsp_2].set_stan(0)  # wróć do stanu 0
        przycisk.config(image="")  # przycisk bez obrazka
    warunki_zakonczenia(window, szerokosc, wysokosc, tab)
    wyswietl['text'] = "Pozostałe bomby do oznaczenia: {}".format(bomby.get_bomby())


def warunki_zakonczenia(window, szerokosc, wysokosc, tab):
    ilosc_bomb = 0
    oznaczone_bomby = 0
    oznaczone = 0
    odsloniete = 0
    wszystkie = szerokosc*wysokosc
    for a in range(wysokosc):
        for b in range(szerokosc):
            # przeliczamy ilość bomb, można przekazać w parametrze
            if tab[a][b].wartosc == BOMBA:
                ilosc_bomb += 1
            # liczymy ile jest oznaczonych flagą
            if tab[a][b].stan == STAN_FLAGI:
                oznaczone += 1
            # porównujemy ilość oznaczonych
            if tab[a][b].wartosc == BOMBA and tab[a][b].stan == STAN_FLAGI:
                oznaczone_bomby += 1
            # liczymy ile odsłoniętych
            if tab[a][b].stan == ODSLONIETY:
                odsloniete += 1
    # jeśli warunki spełnione to przejdź do okna zamknięcia
    if ilosc_bomb == oznaczone_bomby == oznaczone or odsloniete+ilosc_bomb == wszystkie:
        faza_trzecia.faza_trzecia(window, szerokosc, wysokosc, 1)


def kololowanko(wartosc):
    KOLORY = ["blue", "green", "red", "navy", "#8B0000", "#FFFF00", "#DC143C", "black"]
    liczba = "  "
    kolor = stale.SZARY_JASNY
    if 1 <= wartosc <= 8:
        return f"{wartosc}", KOLORY[wartosc - 1]
    else:
        return "  ", stale.SZARY_JASNY


def generuj_pola(window, tab, szerokosc, wysokosc, bomby):  # generowanie planszy
    elementy = window.place_slaves()
    for l in elementy:
        l.destroy()

    # ustalamy szerokość i wysokość każdego pola jako 26 pixeli
    szerokosc_okna = WYMIAR_OKIENKA*szerokosc - 4
    wysokosc_okna = WYMIAR_OKIENKA*wysokosc + 50  # dodatkowe 50 pixeli na menu górne
    frame = tkinter.Frame(window, bg=stale.SZARY_CIEMNY,
                          width=szerokosc_okna, heigh=wysokosc_okna)
    frame.pack_propagate(0)
    frame.place(x=0, y=0)

    wyswietl = tkinter.Label(frame, text="Pozostałe bomby do oznaczenia: {}".format(bomby),
                             bg=stale.SZARY_JASNY, width=28, height=2)
    wyswietl.place(x=40, y=8)

    photo = tkinter.PhotoImage(file='img/retry.png')

    # przycisk do resetowania gry
    reset = tkinter.Button(frame, bg=stale.SZARY_JASNY, width=30, heigh=31,
                           image=photo, command=lambda: zresetuj(window))
    reset.place(x=3, y=8)
    logo = photo.subsample(4, 4)
    reset.config(image=logo)
    reset.image = logo

    board = tkinter.Frame(frame, bg=stale.SZARY_CIEMNY, width=szerokosc_okna,
                          heigh=int(wysokosc_okna-50))
    board.place(x=0, y=50)

    btTablica = []
    liczba_bomb = Dane.Dane()
    liczba_bomb.set_bomby(bomby)
    for i in range(wysokosc):
        temp = []
        for j in range(szerokosc):
            if tab[i][j].stan == 1:  # jeśli jest stan równy 1 ustawiony, to wyświetlaj liczby
                liczba, kolor = kololowanko(tab[i][j].wartosc)
                przycisk = tkinter.Label(board, bg=stale.SZARY_CIEMNY, text="  {}  ".format(liczba),
                                         font=("Calibri", 10), fg='{}'.format(kolor))
            else:
                # tworzymy pusty przycisk
                przycisk = tkinter.Button(board, bg=stale.SZARY_JASNY, text="     ")
                # obsługa lewego kliknięcia
                przycisk.bind("<Button-1>", partial(lewe_klikniecie, window, tab,
                                                    szerokosc, wysokosc, i, j, btTablica))
                # obsługa prawego kliknięcia
                przycisk.bind("<Button-3>", partial(prawe_klikniecie, window, szerokosc, wysokosc,
                                                    tab, i, j, przycisk, wyswietl, liczba_bomb))

            przycisk.place(x=j*WYMIAR_OKIENKA, y=i*WYMIAR_OKIENKA)
            temp.append(przycisk)
        btTablica.append(temp)
