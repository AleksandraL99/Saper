"""Główny plik projektowy"""
import tkinter

from funkcje import laduj_menu
from funkcje import obrazy_i_stale

def main():
    """Główna funkcja"""
    window = tkinter.Tk()
    obrazy_i_stale.Assets.load()
    laduj_menu.laduj_menu(window)

    tkinter.mainloop()

if __name__ == "__main__":
    main()
