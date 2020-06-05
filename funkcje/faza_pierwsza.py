"""Plik obejmujący budowanie okna gry i pierwszy strzał"""
from functools import partial
import tkinter

from funkcje import faza_druga
from pozostale import obrazy_i_stale

WYMIAR_OKIENKA = 26
WYMIAR_RESET = 30


# po pierwszym kliknięciu przejdź do fazy drugiej z tymi samymi parametrami
def pierwszy_klik(window, bomby, dane, wspolrzedna_1, wspolrzedna_2):
    """Funkcja kierująca po kliknięciu do kolejnej fazy"""
    faza_druga.faza_druga(window, bomby, dane, wspolrzedna_1, wspolrzedna_2)


def faza_pierwsza(window, dane, bomby):
    """Funkcja budująca okno gry, przygotowane na pierwszy strzał"""
    print(dane)

    szerokosc, wysokosc = dane  # szerokość i wysokość wczytywana z planszy
    elementy = window.place_slaves()
    for element in elementy:  # niszczymy poprzenie okno
        element.destroy()

    # ustalamy szerokość i wysokość każdego pola jako 26 pixeli
    szerokosc_okna = WYMIAR_OKIENKA*szerokosc - 4
    # dodatkowe 50 pixeli na menu górne
    wysokosc_okna = WYMIAR_OKIENKA*wysokosc + 50
    window.geometry("{}x{}".format(szerokosc_okna, wysokosc_okna))

    frame = tkinter.Frame(window, bg=obrazy_i_stale.SZARY_CIEMNY,
                          width=szerokosc_okna, heigh=wysokosc_okna)
    frame.pack_propagate(0)
    frame.place(x=0, y=0)

    wyswietl = tkinter.Label(frame, text="Pozostałe bomby do oznaczenia: {}".format(bomby),
                             bg=obrazy_i_stale.SZARY_JASNY, width=28, height=2)
    wyswietl.place(x=40, y=8)  # ramka z iloscią bomb do oznaczenia

    photo = obrazy_i_stale.Assets.RESET_OBRAZ

    # przycisk resetu
    reset = tkinter.Button(frame, bg=obrazy_i_stale.SZARY_JASNY,
                           width=WYMIAR_RESET, heigh=WYMIAR_RESET, image=photo)

    reset.place(x=3, y=8)
    logo = photo.subsample(4, 4)
    reset.config(image=logo)
    reset.image = logo

    board = tkinter.Frame(frame, bg=obrazy_i_stale.SZARY_CIEMNY,
                          width=szerokosc_okna, heigh=int(wysokosc_okna-50))
    board.place(x=0, y=50)

    for i in range(wysokosc):
        for j in range(szerokosc):
            # przyciski
            strzal = tkinter.Button(board, bg=obrazy_i_stale.SZARY_JASNY, text="     ",
                                    command=partial(pierwszy_klik, window, bomby, dane, i, j))
            # gdy się wciśnie, to przechodzimy do fazy 2, z danymi współrzędnymi pierwszego strzału
            strzal.place(x=j*WYMIAR_OKIENKA, y=i*WYMIAR_OKIENKA)
