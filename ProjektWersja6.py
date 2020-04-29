from funkcje.ladujMenu import *

def start(menustart):
    menustart.place_forget()


def main():
    window = Tk()    

    ladujMenu(window);

    mainloop()



if __name__ == "__main__":
    main()
