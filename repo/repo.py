from domain.domain import *
from copy import *

class Teatru_file_repo:
    """
    Clasa care este responsabila pentru a mentine persistenta si a face realizabile operatiile necesare cerute de utilizator

    Clasa primeste numele fisierului, incarca datele din fisier in memorie, iar mai apoi realizeaza operatiile cerute
    """
    def __init__(self, filename):
        self.__filename = filename
        self.__teatre = {}
        self.__key = 0
        self.__load()

    def __load(self):
        """
        Incarca datele din fisier in memorie
        """
        with open (self.__filename, "r") as f:
            for line in f:

                line = line.strip()

                if not line:
                    continue

                parts = line.split(";")

                titlu = parts[0]
                regizor = parts[1]
                gen = parts[2]
                durata = parts[3]

                teatru = Teatru(titlu,regizor,gen,durata)

                self.__teatre[self.__key] = teatru
                self.__key += 1

    def __save(self):
        """
        Salveaza datele din fisier in memorie
        """
        with open(self.__filename, "w") as f:
            for teatru in self.__teatre.values():
                f.write(F"{teatru.getTitlu()};{teatru.getRegizor()};{teatru.getGen()};{teatru.getDurata()} \n")

    def save2(self, lista):
        """"
        Salveaza datele din lista(care de fapt e un dictionar in ciuda numelui :) ) primita in fisier
        """
        self.__teatre = deepcopy(lista)
        self.__save()

    def store(self, teatru):
        """
        Salveaza cate o piesa de teatru in memorie, iar mai apoi in fisier
        :param teatru: este o piesa de teatru
        :return:
        """
        self.__teatre[self.__key] = teatru
        self.__key += 1
        self.__save()

    def getAll(self):
        """
        :return: Datele din memorie catre service
        """
        return self.__teatre


