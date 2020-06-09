"""Test funkcji z modułu gra"""
from unittest import TestCase

from funkcje.faza_druga import przelicz
from funkcje.gra import kololowanko, odsloniecia
from klasy.Pole import Pole


class Test(TestCase):
    def setUp(self):
        self.wartosc = 3

    def test_kololowanko(self):
        self.assertEqual(kololowanko(self.wartosc), ("3", "red"))

    def test_odsloniecia(self):
        tablica = []
        for i in range(3):
            tablica.append([])
            for j in range(3):
                pole = Pole()
                pole.set_stan(0)
                pole.set_wartosc(0)
                tablica[i].append(pole)

        tablica[0][2].set_wartosc(9)
        tablica[2][1].set_wartosc(9)

        przelicz(tablica)

        odsloniecia(tablica, 3, 3, 0, 0, [])  # Przypadek odsłaniania po trafieniu w zero
        tablica_porownawcza_1 = [[1, 1, 0], [1, 1, 0], [0, 0, 0]]

        tablica_wypisz = []
        for i, stan in enumerate(tablica):
            tablica_wypisz.append([])
            for j in stan:
                tablica_wypisz[i].append(j.stan)

        self.assertEqual(tablica_wypisz, tablica_porownawcza_1)

        odsloniecia(tablica, 3, 3, 2, 2, [])  # Przypadek odsłaniania po trafieniu w liczbę
        tablica_porownawcza_2 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

        tablica_wypisz = []
        for i, stan in enumerate(tablica):
            tablica_wypisz.append([])
            for j in stan:
                tablica_wypisz[i].append(j.stan)

        self.assertEqual(tablica_wypisz, tablica_porownawcza_2)

    def test_przelicz(self):
        tablica = []
        for i in range(3):
            tablica.append([])
            for j in range(3):
                pole = Pole()
                pole.set_stan(0)
                pole.set_wartosc(0)
                tablica[i].append(pole)

        tablica[0][2].set_wartosc(9)
        tablica[2][1].set_wartosc(9)

        przelicz(tablica)

        tablica_porownawcza = [[0, 1, 9], [1, 2, 2], [1, 9, 1]]

        tablica_wypisz = []
        for i, wartosc in enumerate(tablica):
            tablica_wypisz.append([])
            for j in wartosc:
                tablica_wypisz[i].append(j.wartosc)

        self.assertEqual(tablica_wypisz, tablica_porownawcza)
