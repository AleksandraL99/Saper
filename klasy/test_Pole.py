"""Testy modułu Pole"""
from unittest import TestCase

from klasy.Pole import Pole


class TestPole(TestCase):
    def setUp(self):
        liczba = Pole()
        liczba.set_wartosc(22)
        self.liczba = liczba

    def test_set_wartosc(self):
        self.liczba.set_wartosc(23)
        self.assertEqual(self.liczba.wartosc, 23)
