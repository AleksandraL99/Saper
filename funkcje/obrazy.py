import tkinter


class Assets:
    """Przechowuje zasoby."""

    @staticmethod
    def load():
        """Wczytuje zasoby z dysku."""
        Assets.FLAGA_OBRAZ = tkinter.PhotoImage(file='img/flaga.png')
        Assets.PYTAJNIK_OBRAZ = tkinter.PhotoImage('img/pytajnik.png')
        Assets.RESET_OBRAZ = tkinter.PhotoImage('img/retry.png')

