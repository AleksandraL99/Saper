import tkinter

from funkcje import laduj_menu
from funkcje import obrazy

def main():
    window = tkinter.Tk()
    obrazy.Assets.load()
    laduj_menu.laduj_menu(window)

    tkinter.mainloop()

if __name__ == "__main__":
    main()
