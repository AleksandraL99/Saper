"""Plik w którym dzieje się część gry po pierwszym strzale, ale przed grą właściwą"""
import random

from klasy import Pole
from funkcje import gra

BOMBA = 9
PIERWSZY_WIERSZ_LUB_KOLUMNA = 0


# funkcja losująca bomby, przyjmuje takie argumenty jak
# ilość bomb, szerokość i wysokość planszy oraz współrzędne pierwszego strzału
def losowanie_bomb(bomby, szerokosc, wysokosc, wspolrzedna_1, wspolrzedna_2):
    """Funkcja, w której losują się miejca bomb"""
    # ustalenie numeru pola w które strzelił gracz
    strzelone = wspolrzedna_1*szerokosc+wspolrzedna_2
    pola = list(range(0, strzelone))+list(range(strzelone+1, szerokosc*wysokosc))
    bomb = random.sample(pola, bomby)  # losowanie bomb wśród pozostałych pól

    plansza = [[Pole.Pole() for col in range(szerokosc)] for row in range(wysokosc)]
    for i in bomb:  # przełożenie z numeru pól nas tablice dwuwymiarową
        wsp_1 = i // szerokosc
        wsp_2 = i % szerokosc
        # ustawienie wartości 9 w miejscach pól z bombami
        plansza[wsp_1][wsp_2].set_wartosc(BOMBA)
    return plansza  # zwraca tablicę z oznaczonymi polami bomb


# funkcja przeliczająca numery pojawiające się w danym polu
def przelicz(plansza):
    """Funkcja przeliczająca wartości pojawiające się na polach"""
    for i, wiersz in enumerate(plansza):
        for j, pole in enumerate(wiersz):
            n_bomb = 0
            if pole.wartosc == BOMBA:
                continue
            for di in (-1, 0, +1):
                for dj in (-1, 0, +1):
                    if di == dj == 0:
                        continue
                    if not 0 <= i + di < len(plansza):
                        continue
                    if not 0 <= j + dj < len(wiersz):
                        continue
                    if plansza[i+di][j+dj].wartosc == BOMBA:
                        n_bomb += 1
            pole.set_wartosc(n_bomb)


def faza_druga(window, bomby, dane, wspolrzedna_1, wspolrzedna_2):
    """Faza obejmująca wykananie losowania bomba, przeliczenia pól i wygenerowania planszy"""
    szerokosc, wysokosc = dane
    bomb = losowanie_bomb(bomby, szerokosc, wysokosc, wspolrzedna_1, wspolrzedna_2)

    przelicz(bomb)  # nadanie wartości w tablicy

    odslon = []  # tworzymy pustą tablice odsłonięć
    gra.odsloniecia(bomb, szerokosc, wysokosc, wspolrzedna_1, wspolrzedna_2, odslon)

    # przechodzimy do gry właściwej
    gra.generuj_pola(window, bomb, szerokosc, wysokosc, bomby)
