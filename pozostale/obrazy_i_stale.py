"""Plik zawierający obrazy i stałe"""
import tkinter


SZARY_JASNY = "#C0C0C0"
SZARY_CIEMNY = "#808080"
CZCIONKA = "Calibri"


class Assets:
    """Przechowuje zasoby."""

    @staticmethod
    def load():
        """Wczytuje zasoby z dysku."""
        Assets.FLAGA_OBRAZ = tkinter.PhotoImage(file='img/flaga.png')
        Assets.PYTAJNIK_OBRAZ = tkinter.PhotoImage(file='img/pytajnik.png')
        Assets.RESET_OBRAZ = tkinter.PhotoImage(file='img/retry.png')
