import tkinter

from funkcje import laduj_menu
from funkcje import obrazy_i_stale

def main():
    window = tkinter.Tk()
    obrazy_i_stale.Assets.load()
    laduj_menu.laduj_menu(window)

    tkinter.mainloop()

if __name__ == "__main__":
    main()
