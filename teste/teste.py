from domain.domain import Teatru, Teatru_validator
from repo.repo import Teatru_file_repo
from service.service import Service


def test_Create_teatru():
    """
    Testam daca funcitea creaza corect o piesa de teatru

    Functia primeste titlu, regizor, gen, durata, iar apoi daca sunt valide creaza piesa de teatru
        """
    open("test_teatre.txt", 'w').close()
    repo = Teatru_file_repo("test_teatre.txt")
    validator = Teatru_validator()
    service = Service(repo, validator)

    titlu = "ceva1"
    regizor = "ceva2"
    gen = "Drama"
    durata = 3

    service.Create_teatru(titlu, regizor, gen, durata)

    with open("test_teatre.txt", "r") as f:
        linie = f.readlines()

    assert linie[0] == "ceva1;ceva2;Drama;3 \n"

    print("Piesa a fost adaugat cu succes")

    open("test_teatre.txt", 'w').close()

def test_Modify_teatrU():
    """
    Testam daca functia modifica corect o piesa de teatru

    Functia primeste titlu, regizor, gen, durata. Verifica daca exsita deja piesa de teatru, apoi o modifica
    """
    open("test_teatre.txt", 'w').close()
    repo = Teatru_file_repo("test_teatre.txt")
    validator = Teatru_validator()
    service = Service(repo, validator)

    titlu = "ceva1"
    regizor = "ceva2"
    gen = "Drama"
    durata = 3
    service.Create_teatru(titlu, regizor, gen, durata)
    service.Modify_teatru("ceva1", "ceva2", "Comedie", 5)
    try:
        service.Modify_teatru("ceva1", "ceva3", "Comedie", 5)
    except Exception as e:
        print(e)

    with open("test_teatre.txt", "r") as f:
        linie = f.readlines()

    assert linie[0] == "ceva1;ceva2;Comedie;5 \n"

    print("Piesa a fost modificat cu succes")

    open("test_teatre.txt", 'w').close()

def test_Generate():
    """
    Verificam daca functia genereaza corect piesele de teatru

    Functia primeste un paramentru n si genereaza n piese de teatru
    """
    open("test_teatre.txt", 'w').close()
    repo = Teatru_file_repo("test_teatre.txt")
    validator = Teatru_validator()
    service = Service(repo, validator)


    service.Generate(3)

    with open("test_teatre.txt", "r") as f:
        linie = f.readlines()

    assert len(linie) == 3

    print("Piesele au fost generate cu succes")

    open("test_teatre.txt", 'w').close()

def rulare_teste():
    test_Create_teatru()
    test_Modify_teatrU()
    test_Generate()
    print("Testele au rulat cu succes!",'\n')