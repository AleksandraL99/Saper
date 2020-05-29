from functools import partial
import tkinter

from funkcje import laduj_menu
from funkcje import stale

WYMIAR_OKIENKA = 26
ROZMIAR_TEKSTU = 25


def reset(window):
    elementy = window.place_slaves()
    for l in elementy:
        l.destroy()
    laduj_menu.laduj_menu(window)


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

    menu = tkinter.Frame(window, bg=stale.SZARY_CIEMNY, width=width, heigh=height)
    menu.pack_propagate(0)
    menu.place(x=0, y=0)

    if status == 1:  # Jeśli status to 1, to oznacza wygraną
        label = tkinter.Label(menu, text="Wygrałeś", bg=stale.SZARY_JASNY,
                              width=10, font=(stale.CZCIONKA, ROZMIAR_TEKSTU))
        label.place(x=pozycja1, y=pozycja2)
    else:  # Jeśli status jest inny, to oznacza przegraną
        label = tkinter.Label(menu, text="Przegrałeś", bg=stale.SZARY_JASNY,
                              width=10, font=(stale.CZCIONKA, ROZMIAR_TEKSTU))
        label.place(x=pozycja1, y=pozycja2)

    sprobuj_ponownie = tkinter.Button(menu, bg=stale.SZARY_JASNY, heigh=1,
                                      text="Zagraj ponownie", command=lambda: reset(window))
    sprobuj_ponownie.place(x=szerokosc_okna/2-45, y=7*wysokosc_okna/10)

    zakoncz = tkinter.Button(menu, bg=stale.SZARY_JASNY, width=10, heigh=1,
                             text="Zakończ grę", command=lambda: window.destroy())
    zakoncz.place(x=szerokosc_okna/2-35, y=4*wysokosc_okna/5)
