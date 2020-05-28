from random import sample

import klasy.Pole
import funkcje.gra

BOMBA = 9
PIERWSZY_WIERSZ_LUB_KOLUMNA = 0


# funkcja losująca bomby, przyjmuje takie argumenty jak
# ilość bomb, szerokość i wysokość planszy oraz współrzędne pierwszego strzału
def losowanie_bomb(bomby, szerokosc, wysokosc, wspolrzedna_1, wspolrzedna_2):
    # ustalenie numeru pola w które strzelił gracz
    strzelone = wspolrzedna_1*szerokosc+wspolrzedna_2
    pola = list(range(0, strzelone))+list(range(strzelone+1, szerokosc*wysokosc))
    bomb = sample(pola, bomby)  # losowanie bomb wśród pozostałych pól

    tab = [[klasy.Pole.Pole() for col in range(szerokosc)] for row in range(wysokosc)]
    for i in bomb:  # przełożenie z numeru pól nas tablice dwuwymiarową
        wsp_1 = i // szerokosc
        wsp_2 = i % szerokosc
        # ustawienie wartości 9 w miejscach pól z bombami
        tab[wsp_1][wsp_2].set_wartosc(BOMBA)
    return tab  # zwraca tablicę z oznaczonymi polami bomb


# funkcja przeliczająca numery pojawiające się w danym polu
def przelicz(tab, szerokosc, wysokosc):
    for w_wysokosci in range(wysokosc):
        for w_szerokosci in range(szerokosc):
            i = 0  # licznik do liczenia bomb w sąsiedztwie
            # nie przelicza jeśli już ma wartość bomby
            if tab[w_wysokosci][w_szerokosci].wartosc == BOMBA:
                pass
            else:
                # na prawo
                if w_szerokosci != szerokosc-1 and tab[w_wysokosci][w_szerokosci+1].wartosc == BOMBA:
                    i = i+1
                # na lewo
                if w_szerokosci != PIERWSZY_WIERSZ_LUB_KOLUMNA and tab[w_wysokosci][w_szerokosci-1].wartosc == BOMBA:
                    i = i+1
                # dół
                if w_wysokosci != wysokosc-1 and tab[w_wysokosci+1][w_szerokosci].wartosc == BOMBA:
                    i = i+1
                # góra
                if w_wysokosci != PIERWSZY_WIERSZ_LUB_KOLUMNA and tab[w_wysokosci-1][w_szerokosci].wartosc == BOMBA:
                    i = i+1
                # prawy dolny róg
                if w_wysokosci != wysokosc-1 and w_szerokosci != szerokosc-1 and tab[w_wysokosci+1][w_szerokosci+1].wartosc == BOMBA:
                    i = i+1
                # lewy doly róg
                if w_wysokosci != wysokosc-1 and w_szerokosci != PIERWSZY_WIERSZ_LUB_KOLUMNA and tab[w_wysokosci+1][w_szerokosci-1].wartosc == BOMBA:
                    i = i+1
                # prawy górny róg
                if w_wysokosci != PIERWSZY_WIERSZ_LUB_KOLUMNA and w_szerokosci != szerokosc-1 and tab[w_wysokosci-1][w_szerokosci+1].wartosc == BOMBA:
                    i = i+1
                # lewy dolny róg
                if w_wysokosci != PIERWSZY_WIERSZ_LUB_KOLUMNA and w_szerokosci != PIERWSZY_WIERSZ_LUB_KOLUMNA and tab[w_wysokosci-1][w_szerokosci-1].wartosc == BOMBA:
                    i = i+1
                # ustawiamy taką wartość, jaką obliczyliśmy
                tab[w_wysokosci][w_szerokosci].set_wartosc(i)


def faza_druga(window, bomby, dane, wspolrzedna_1, wspolrzedna_2):
    szerokosc, wysokosc = dane
    bomb = losowanie_bomb(bomby, szerokosc, wysokosc, wspolrzedna_1, wspolrzedna_2)
    przelicz(bomb, szerokosc, wysokosc)  # nadanie wartości w tablicy

    odslon = []  # tworzymy pustą tablice odsłonięć
    funkcje.gra.odsloniecia(bomb, szerokosc, wysokosc, wspolrzedna_1, wspolrzedna_2, odslon)

    for i in bomb:
        for j in i:
            print(j.wartosc, end=" ")
        print()
    print()

    for i in bomb:
        for j in i:
            print(j.stan, end="")
        print()
    # przechodzimy do gry właściwej
    funkcje.gra.generuj_pola(window, bomb, szerokosc, wysokosc, bomby)
