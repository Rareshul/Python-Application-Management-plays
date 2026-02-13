import random
from repo.repo import *

class Service:
    """
    Clasa care este responsabila pentru primirea, validarea, manipularea si trimiterea datelor repository-ului pentru a fi salvate in fisier, sau adaugate

    Are mai multe functii, care sunt apelate in main
    """
    def __init__(self, repo, validator):
        self.repo = repo
        self.validator = validator

    def Create_teatru(self, titlu, regizor, gen, durata):
        """
        Creaza si trimite spre validate o piesa de teatru

        Parametrii sunt string-uri sau int primite din main de la utilizator

        :return:
        """
        teatru = Teatru(titlu,regizor,gen,durata)

        if self.validator != None:
            self.validator.validate(teatru)

        self.repo.store(teatru)

    def Modify_teatru(self, titlu, regizor, gen, durata):
        """
        Modifica o piesa de teatru deja existenta

        Parametrii sunt string-uri sau int primite din main de la utilizator:

        """
        list = self.repo.getAll()
        bool = 0

        for teatru in list.values():
            Titlu = teatru.getTitlu()
            Regizor = teatru.getRegizor()
            if Titlu == titlu and Regizor == regizor:
                teatru.setGen(gen)
                teatru.setDurata(durata)
                bool = 1

        if bool == 1:
            self.repo.save2(list)
        else:
            raise ValueError("Piesa nu exista")

    def Generate(self, numar):
        """
        Genereaza random piese de teatru, iar mai apoi le salveaza in memorie si fisier
        :param numar: este un int primit de la utilizator care indica nr. de piese generate
        """
        dict = {}
        vocale = "aeiouAEIOU"
        consoane = []
        gen_sir = ["Comedie", "Drama", "Satir", "Altele"]
        string_generat =""

        for i in range(ord('a'), ord('z')):
            caracter = chr(i)
            if caracter not in "aeiou":
                consoane.append(caracter)

        for i in range(ord('A'), ord('Z')):
            caracter = chr(i)
            if caracter not in "AEIOU":
                consoane.append(caracter)

        for i in range (numar):
            for j in range (2):
                string_generat = ""
                lungime = random.randrange(8,11)
                mijloc = lungime // 2

                for i in range(mijloc):
                    string_generat += random.choice(consoane)
                    string_generat += random.choice(vocale)

                string_generat += " "

                for i in range(lungime-mijloc-1):
                    string_generat += random.choice(consoane)
                    string_generat += random.choice(vocale)
                if j == 0:
                    titlu = string_generat

                if j == 1:
                    regizor = string_generat

            gen = random.choice(gen_sir)
            durata = random.randrange(0, 11)

            teatru = Teatru(titlu, regizor, gen, durata)

            self.repo.store(teatru)


