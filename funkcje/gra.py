"""Plik gry właściwej"""
import tkinter
from functools import partial

from funkcje import faza_trzecia
from funkcje import laduj_menu
from funkcje import obrazy_i_stale
from klasy import Dane

ODSLONIETY = 1
NIEODSLONIETY = 0
STAN_FLAGI = 2
STAN_PYTAJNIKA = 3
WYMIAR_OKIENKA = 26
BOMBA = 9
PUSTY = 0


def zresetuj(window):
    """Funkcja resetowania gry"""
    elementy = window.place_slaves()
    for element in elementy:
        element.destroy()
    laduj_menu.laduj_menu(window)


def odsloniecia(plansza, szerokosc, wysokosc, wsp_1, wsp_2, odslon):
    """funkcja odsłaniajaca po kliknięciu"""
    # jeśli trafi się w pole z wartością 0 (pustą) i nieodsłoniętą, to idź rekurencyjnie
    if plansza[wsp_1][wsp_2].wartosc == PUSTY and plansza[wsp_1][wsp_2].stan == NIEODSLONIETY:
        plansza[wsp_1][wsp_2].set_stan(1)  # ustaw stan na odsłonięcie
        odslon.append((wsp_1, wsp_2))  # odsłoń
        if wsp_1 != 0:  # jeśli to nie jest element w zerowym wierszu
            # to idź rekurencyjnie do góry
            odsloniecia(plansza, szerokosc, wysokosc, wsp_1-1, wsp_2, odslon)
        if wsp_1 != wysokosc-1:  # jeśli to nie ostatni wiersz
            # to idź do dołu
            odsloniecia(plansza, szerokosc, wysokosc, wsp_1+1, wsp_2, odslon)
        if wsp_2 != 0:  # jeśli to nie zerowa kolumna
            # to idź w lewo
            odsloniecia(plansza, szerokosc, wysokosc, wsp_1, wsp_2-1, odslon)
        if wsp_2 != szerokosc-1:  # jeśli to nie ostatnia kolumna
            # to idź w prawo
            odsloniecia(plansza, szerokosc, wysokosc, wsp_1, wsp_2+1, odslon)
    else:  # jeśli trafimy na komórkę z wartością lub już odsłoniętą
        plansza[wsp_1][wsp_2].set_stan(ODSLONIETY)  # zmień stan na odsłonięty
        odslon.append((wsp_1, wsp_2))  # odsłoń ją
        # lewy górny róg
        if (wsp_1 != 0 and wsp_2 != szerokosc-1 and
                plansza[wsp_1][wsp_2+1].wartosc == PUSTY and
                plansza[wsp_1-1][wsp_2].wartosc != PUSTY and
                plansza[wsp_1][wsp_2+1].stan == ODSLONIETY):
            plansza[wsp_1-1][wsp_2].set_stan(1)  # ustaw stan 1
            odslon.append((wsp_1-1, wsp_2))
        # prawy dolny róg
        if (wsp_1 != wysokosc-1 and wsp_2 != 0 and
                plansza[wsp_1][wsp_2-1].wartosc == PUSTY and
                plansza[wsp_1+1][wsp_2].wartosc != PUSTY and
                plansza[wsp_1][wsp_2-1].stan == ODSLONIETY):
            plansza[wsp_1+1][wsp_2].set_stan(ODSLONIETY)
            odslon.append((wsp_1+1, wsp_2))
        # lewy dolny róg
        if (wsp_1 != wysokosc-1 and wsp_2 != szerokosc-1 and
                plansza[wsp_1][wsp_2+1].wartosc == PUSTY and
                plansza[wsp_1+1][wsp_2].wartosc != PUSTY and
                plansza[wsp_1][wsp_2+1].stan == ODSLONIETY):
            plansza[wsp_1+1][wsp_2].set_stan(ODSLONIETY)
            odslon.append((wsp_1+1, wsp_2))
        # prawy górny róg
        if (wsp_1 != 0 and wsp_2 != 0 and plansza[wsp_1][wsp_2-1].wartosc == PUSTY and
                plansza[wsp_1-1][wsp_2].wartosc != PUSTY and
                plansza[wsp_1][wsp_2-1].stan == ODSLONIETY):
            plansza[wsp_1-1][wsp_2].set_stan(ODSLONIETY)
            odslon.append((wsp_1-1, wsp_2))


def lewe_klikniecie(window, plansza, szerokosc, wysokosc, wsp_1, wsp_2, btTablica, self):
    """Funkcja obsługi kliknięcia lewego"""
    if plansza[wsp_1][wsp_2].stan == NIEODSLONIETY:  # jeśli nieodkryty
        if plansza[wsp_1][wsp_2].wartosc == 9:
            faza_trzecia.faza_trzecia(window, szerokosc, wysokosc, 0)
            print("end")
            return
        odslon = []
        odsloniecia(plansza, szerokosc, wysokosc, wsp_1, wsp_2, odslon)
        for i, j in odslon:
            liczba, kolor = kololowanko(plansza[i][j].wartosc)
            lb = tkinter.Label(btTablica[i][j].master, bg=obrazy_i_stale.SZARY_CIEMNY,
                               text="  {}  ".format(liczba),
                               font=("Calibri", 10), fg='{}'.format(kolor))
            lb.place(x=j*26, y=i*26)
            btTablica[i][j].destroy()
        warunki_zakonczenia(window, szerokosc, wysokosc, plansza)
    else:
        print("Tu jest flaga/znak zapytania, nie da się strzelić")


def prawe_klikniecie(window, szerokosc, wysokosc,
                     plansza, wsp_1, wsp_2, przycisk, wyswietl, bomby, self):
    """Funkcja obsługi prawego kliknięcia"""
    # w tej części możemy użyć flagi i pytajnika

    if plansza[wsp_1][wsp_2].stan == NIEODSLONIETY:  # jeśli jeszcze nie był klikany
        plansza[wsp_1][wsp_2].set_stan(STAN_FLAGI)  # ustaw stan 2, odpowiedzialny za flagę)
        logo = obrazy_i_stale.Assets.FLAGA_OBRAZ.subsample(2, 2)
        przycisk.config(image=logo)  # stwórz przycisk z obrazkiem plagi
        przycisk.image = logo
        bomby.set_bomby(bomby.get_bomby()-1)
    elif plansza[wsp_1][wsp_2].stan == STAN_FLAGI:  # jeśli stanem było 2 (flaga)
        plansza[wsp_1][wsp_2].set_stan(STAN_PYTAJNIKA)  # ustaw stan 3, czyli pytajnik
        logo = obrazy_i_stale.Assets.PYTAJNIK_OBRAZ.subsample(2, 2)
        przycisk.config(image=logo)  # stwórz przycisk z pytajnikiem
        przycisk.image = logo
        bomby.set_bomby(bomby.get_bomby()+1)
    elif plansza[wsp_1][wsp_2].stan == STAN_PYTAJNIKA:  # jeśli stanem było 3 (pytajnik)
        plansza[wsp_1][wsp_2].set_stan(NIEODSLONIETY)  # wróć do stanu 0
        przycisk.config(image="")  # przycisk bez obrazka
    warunki_zakonczenia(window, szerokosc, wysokosc, plansza)
    wyswietl['text'] = "Pozostałe bomby do oznaczenia: {}".format(bomby.get_bomby())


def warunki_zakonczenia(window, szerokosc, wysokosc, plansza):
    """Funkcja sprawdzająca warunki zakończenia"""
    ilosc_bomb = 0
    oznaczone_bomby = 0
    oznaczone = 0
    odsloniete = 0
    wszystkie = szerokosc*wysokosc
    for i in range(wysokosc):
        for j in range(szerokosc):
            # przeliczamy ilość bomb, można przekazać w parametrze
            if plansza[i][j].wartosc == BOMBA:
                ilosc_bomb += 1
            # liczymy ile jest oznaczonych flagą
            if plansza[i][j].stan == STAN_FLAGI:
                oznaczone += 1
            # porównujemy ilość oznaczonych
            if plansza[i][j].wartosc == BOMBA and plansza[i][j].stan == STAN_FLAGI:
                oznaczone_bomby += 1
            # liczymy ile odsłoniętych
            if plansza[i][j].stan == ODSLONIETY:
                odsloniete += 1
    # jeśli warunki spełnione to przejdź do okna zamknięcia
    if ilosc_bomb == oznaczone_bomby == oznaczone or odsloniete+ilosc_bomb == wszystkie:
        faza_trzecia.faza_trzecia(window, szerokosc, wysokosc, 1)


def kololowanko(wartosc):
    """Funkcja nadająca kolor i wartość odsłanianym polom"""
    KOLORY = ["blue", "green", "red", "navy", "#8B0000", "#FFFF00", "#DC143C", "black"]
    liczba = "  "
    kolor = obrazy_i_stale.SZARY_JASNY
    if 1 <= wartosc <= 8:
        return f"{wartosc}", KOLORY[wartosc - 1]
    else:
        return "  ", obrazy_i_stale.SZARY_JASNY


def generuj_pola(window, plansza, szerokosc, wysokosc, bomby):  # generowanie planszy
    """Funkcja genrująca planszę"""
    elementy = window.place_slaves()
    for l in elementy:
        l.destroy()

    # ustalamy szerokość i wysokość każdego pola jako 26 pixeli
    szerokosc_okna = WYMIAR_OKIENKA*szerokosc - 4
    wysokosc_okna = WYMIAR_OKIENKA*wysokosc + 50  # dodatkowe 50 pixeli na menu górne
    frame = tkinter.Frame(window, bg=obrazy_i_stale.SZARY_CIEMNY,
                          width=szerokosc_okna, heigh=wysokosc_okna)
    frame.pack_propagate(0)
    frame.place(x=0, y=0)

    wyswietl = tkinter.Label(frame, text="Pozostałe bomby do oznaczenia: {}".format(bomby),
                             bg=obrazy_i_stale.SZARY_JASNY, width=28, height=2)
    wyswietl.place(x=40, y=8)

    photo = obrazy_i_stale.Assets.RESET_OBRAZ

    # przycisk do resetowania gry
    reset = tkinter.Button(frame, bg=obrazy_i_stale.SZARY_JASNY, width=30, heigh=31,
                           image=photo, command=lambda: zresetuj(window))
    reset.place(x=3, y=8)
    logo = photo.subsample(4, 4)
    reset.config(image=logo)
    reset.image = logo

    board = tkinter.Frame(frame, bg=obrazy_i_stale.SZARY_CIEMNY, width=szerokosc_okna,
                          heigh=int(wysokosc_okna-50))
    board.place(x=0, y=50)

    btTablica = []
    liczba_bomb = Dane.Dane()
    liczba_bomb.set_bomby(bomby)
    for i in range(wysokosc):
        temp = []
        for j in range(szerokosc):
            # jeśli jest stan równy 1 ustawiony, to wyświetlaj liczby
            if plansza[i][j].stan == ODSLONIETY:
                liczba, kolor = kololowanko(plansza[i][j].wartosc)
                przycisk = tkinter.Label(board, bg=obrazy_i_stale.SZARY_CIEMNY,
                                         text="  {}  ".format(liczba),
                                         font=("Calibri", 10), fg='{}'.format(kolor))
            else:
                # tworzymy pusty przycisk
                przycisk = tkinter.Button(board, bg=obrazy_i_stale.SZARY_JASNY, text="     ")
                # obsługa lewego kliknięcia
                przycisk.bind("<Button-1>", partial(lewe_klikniecie, window, plansza,
                                                    szerokosc, wysokosc, i, j, btTablica))
                # obsługa prawego kliknięcia
                przycisk.bind("<Button-3>", partial(prawe_klikniecie, window, szerokosc, wysokosc,
                                                    plansza, i, j, przycisk, wyswietl, liczba_bomb))

            przycisk.place(x=j*WYMIAR_OKIENKA, y=i*WYMIAR_OKIENKA)
            temp.append(przycisk)
        btTablica.append(temp)
