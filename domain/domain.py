class Teatru:
    """
    Clasa responsabila cu piesele de teatru
    """
    def __init__(self, titlu, regizor, gen, durata):
        self.__titlu = titlu
        self.__regizor = regizor
        self.__gen = gen
        self.__durata = durata

    def getTitlu(self):
        return self.__titlu

    def getRegizor(self):
        return self.__regizor

    def getGen(self):
        return self.__gen

    def getDurata(self):
        return self.__durata

    def setTitlu(self, titlu):
        self.__titlu = titlu

    def setRegizor(self, regizor):
        self.__regizor = regizor

    def setGen(self, gen):
        self.__gen = gen

    def setDurata(self, durata):
        self.__durata = durata

class Teatru_validator:
    """
    Clasa care valideaza datele clasei Teatru
    """
    def validate(self, teatru):

        errors = ""

        if teatru.getTitlu() == "":
            errors += "Titlu nu poate fi gol "

        if teatru.getRegizor() == "":
            errors +=  "Regizorul nu poate fi gol "

        if teatru.getGen() == "":
            errors += "Genul nu poate fi gol "

        if teatru.getDurata() == "":
            errors += "Durata nu poate fi goala "

        if teatru.getDurata() < 0:
            errors += "Durata nu poate fi negativa "

        if teatru.getGen() == "Comedie" or teatru.getGen() == "Drama" or teatru.getGen() == "Satir" or teatru.getGen() == "Altele":
            errors += "Genul nu este corespunzator "

        if errors != "":
            raise ValueError(errors)


