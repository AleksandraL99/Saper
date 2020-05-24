from functools import partial
from tkinter import *

import funkcje.laduj_menu as test
from klasy.Pole import *
from tkinter.font import *


WYMIAR_OKIENKA = 26
ROZMIAR_TEKSTU = 25


def reset(window):
    elementy = window.place_slaves()
    for l in elementy:
        l.destroy()
    test.laduj_menu(window)


def faza_trzecia(window, szerokosc, wysokosc, status):

    szerokosc_okna = WYMIAR_OKIENKA*szerokosc - 4
    wysokosc_okna = WYMIAR_OKIENKA*wysokosc + 50
    # tworzymy okno z startowym menu
    window.geometry("{}x{}".format(szerokosc_okna, wysokosc_okna))
    window.title("Saper")  # z tytułem saper
    height = window.winfo_screenheight()
    width = window.winfo_screenwidth()
    pozycja1 = szerokosc_okna/2-85
    pozycja2 = wysokosc_okna/6

    menu = Frame(window, bg="#808080", width=width, heigh=height)
    menu.pack_propagate(0)
    menu.place(x=0, y=0)

    if status == 1:  # Jeśli status to 1, to oznacza wygraną
        label = Label(menu, text="Wygrałeś", bg="#C0C0C0", width=10, font=("Calibri", ROZMIAR_TEKSTU))
        label.place(x=pozycja1, y=pozycja2)
    else:  # Jeśli status jest inny, to oznacza przegraną
        label = Label(menu, text="Przegrałeś", bg="#C0C0C0", width=10, font=("Calibri", ROZMIAR_TEKSTU))
        label.place(x=pozycja1, y=pozycja2)

    sprobuj_ponownie = Button(menu, bg="#C0C0C0", heigh=1, text="Zagraj ponownie", command=lambda: reset(window))
    sprobuj_ponownie.place(x=szerokosc_okna/2-45, y=7*wysokosc_okna/10)

    zakoncz = Button(menu, bg="#C0C0C0", width=10, heigh=1, text="Zakończ grę", command=lambda: window.destroy())
    zakoncz.place(x=szerokosc_okna/2-35, y=4*wysokosc_okna/5)
