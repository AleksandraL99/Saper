from functools import partial
from tkinter import *

from funkcje.faza_druga import *

WYMIAR_OKIENKA = 26
WYMIAR_RESET = 30


# po pierwszym kliknięciu przejdź do fazy drugiej z tymi samymi parametrami
def pierwszy_klik(window, bomby, dane, wspolrzedna_1, wspolrzedna_2):
    faza_druga(window, bomby, dane, wspolrzedna_1, wspolrzedna_2)


def faza_pierwsza(window, dane, bomby):
    print(dane)

    szerokosc, wysokosc = dane  # szerokość i wysokość wczytywana z planszy
    elementy = window.place_slaves()
    for l in elementy:  # niszczymy poprzenie okno
        l.destroy()

    # ustalamy szerokość i wysokość każdego pola jako 26 pixeli
    szerokosc_okna = WYMIAR_OKIENKA*szerokosc - 4
    # dodatkowe 50 pixeli na menu górne
    wysokosc_okna = WYMIAR_OKIENKA*wysokosc + 50
    window.geometry("{}x{}".format(szerokosc_okna, wysokosc_okna))

    frame = Frame(window, bg="#808080", width=szerokosc_okna, heigh=wysokosc_okna)
    frame.pack_propagate(0)
    frame.place(x=0, y=0)

    wyswietl = Label(frame, text="Pozostałe bomby do oznaczenia: {}".format(bomby), bg="#C0C0C0", width=28, height=2)
    wyswietl.place(x=40, y=8)  # ramka z iloscią bomb do oznaczenia

    photo = PhotoImage(file='img/retry.png') 

    # przycisk resetu
    reset = Button(frame, bg="#C0C0C0", width=WYMIAR_RESET, heigh=WYMIAR_RESET, image=photo, compound=LEFT)
    reset.place(x=3, y=8)

    board = Frame(frame, bg="#808080", width=szerokosc_okna, heigh=int(wysokosc_okna-50))
    board.place(x=0, y=50)

    tab = [[j % 9 for j in range(wysokosc)] for i in range(szerokosc)]
    for i in range(wysokosc):
        for j in range(szerokosc):
            # przyciski
            strzal = Button(board, bg="#C0C0C0", text="     ", command=partial(pierwszy_klik, window, bomby, dane, i, j))
            # gdy się wciśnie, to przechodzimy do fazy 2, z znanymi współrzędnymi pierwszego strzału
            strzal.place(x=j*WYMIAR_OKIENKA, y=i*WYMIAR_OKIENKA)
