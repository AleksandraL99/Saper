import tkinter

import funkcje.laduj_menu
import funkcje.obrazy

def main():
    window = tkinter.Tk()
    funkcje.obrazy.Assets.load()
    funkcje.laduj_menu.laduj_menu(window)

    tkinter.mainloop()

if __name__ == "__main__":
    main()
