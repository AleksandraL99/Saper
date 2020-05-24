class Dane():

    def __init__(self):
        pass

    def set_ustawienia_planszy(self, x, y):
        self.__spix = x
        self.__spiy = y

    def get_ustawienia_planszy(self):
        return (self.__spix, self.__spiy)

    def set_bomby(self, bomby):
        self.__bomby = bomby

    def get_bomby(self):
        return self.__bomby
