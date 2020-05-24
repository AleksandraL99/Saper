from tkinter import *

from funkcje.faza_pierwsza import *
from klasy.Dane import *

OD = 10
DO = 25
SZEROKOŚĆ = 30
WYSOKOŚĆ = 1


def zmiana_pol_poziom(self, dane, bomby):
    # ustawiamy rozmiar planszy zgodnie z tym co zostało wybrane w menu
    spix, spiy = dane.get_ustawienia_planszy()  # spix to szerokosc
    spix = int(self.get())
    bomby.config(from_=int(spix*spiy*0.2), to=int(spix*spiy*0.7))
    dane.set_ustawienia_planszy(spix, spiy)


def zmiana_pol_pion(self, dane, bomby):
    spix, spiy = dane.get_ustawienia_planszy()
    spiy = int(self.get())
    bomby.config(from_=int(spix*spiy*0.2), to=int(spix*spiy*0.7))
    dane.set_ustawienia_planszy(spix, spiy)

def laduj_menu(window):
    dane = Dane()  # startowa szerokość planszy
    dane.set_ustawienia_planszy(10, 10)  # metoda z klasy Dane

    window.geometry("{}x{}".format(250, 300))  # tworzymy okno z startowym menu
    window.title("Saper")  # z tytułem saper
    height = window.winfo_screenheight()
    width = window.winfo_screenwidth()

    # zczytujemy rozmiar ekranu (możliwa opcja późniejszego dopasowania okna)
    print("\n width x height = %d x %d (in pixels)\n" % (width, height))
    menu = Frame(window, bg="#808080", width=width, heigh=height)
    menu.pack_propagate(0)
    menu.place(x=0, y=0)

    label = Label(menu, text="Wybierz wielkość pola", bg="#808080", width=SZEROKOŚĆ, height=WYSOKOŚĆ)
    label.place(x=10, y=20)

    # pole wyboru wysokości
    wybor_wysokosci = Spinbox(menu, from_=OD, to=DO, state="readonly", command=lambda: zmiana_pol_poziom(wybor_wysokosci, dane, wybor_ilosci_bomb))
    wybor_wysokosci.place(x=50, y=55)

    # pole wyboru szerokości
    wybor_szerokosci = Spinbox(menu, from_=OD, to=DO, state="readonly", command=lambda: zmiana_pol_pion(wybor_szerokosci, dane, wybor_ilosci_bomb))
    wybor_szerokosci.place(x=50, y=80)

    label = Label(menu, text="Wybierz ilość bomb", bg="#808080", width=SZEROKOŚĆ, height=WYSOKOŚĆ)
    label.place(x=10, y=120)

    wybor_ilosci_bomb = Spinbox(menu, from_=20, to=70, state="readonly")  # pole wyboru ilości bomb
    wybor_ilosci_bomb.place(x=50, y=150)

    przycisk_dalej = Button(menu, bg="#C0C0C0", width=10, heigh=WYSOKOŚĆ, command=lambda: faza_pierwsza(window, dane.get_ustawienia_planszy(), int(wybor_ilosci_bomb.get())), text="Zatwierdź")
    przycisk_dalej.place(x=75, y=190)  # przycisk do przejścia dalej
