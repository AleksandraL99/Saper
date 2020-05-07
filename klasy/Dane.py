class Dane():

    def __init__(self):
        pass

    def setUstawieniaPlanszy(self,x,y):
        self.__spix = x
        self.__spiy = y
    
    def getUstawieniaPlanszy(self):
        return (self.__spix,self.__spiy)

    def setBomby(self,bomby):
        self.__bomby = bomby

    def getBomby(self):
        return self.__bomby
    


