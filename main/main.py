
from service.service import *
from teste.teste import rulare_teste

repo = Teatru_file_repo("teatre.txt")
validator = Teatru_validator()
service = Service(repo, validator)


while True:

    rulare_teste()
    print("1. Adauga piesa")
    print("2. Modifica piesa")
    print("3. Generarea aleatorie")
    try:
        try:
            optiune = int(input("Optiunea dorita este: "))
        except:
            raise ValueError("Optiunea nu este valida")
    except Exception as e:
        print("Eroate: ", e)
        continue

    if optiune == 1:
        try:
            titlu = input("Titlu este: ")
            regizor = input("Regizorul este: ")
            gen = input("Genul este: ")

            try:
                durata = int(input("Durata este: "))
            except:
                print("Durata nu este valida, trebuie sa fie intreg")
                continue

            service.Create_teatru(titlu, regizor, gen, durata)
        except Exception as e:
            print("Eroare: ", e)
            continue
    if optiune == 2:
        try:
            titlu = input("Titlu este: ")
            regizor = input("Regizorul este: ")
            gen = input("Genul este: ")

            try:
                durata = int(input("Durata este: "))
            except:
                print("Durata nu este valida, trebuie sa fie intreg")
                continue

            service.Modify_teatru(titlu, regizor, gen, durata)

        except Exception as e:
            print("Eroare: ", e)
            continue
    if optiune == 3:
        try:
            try:
                numar = int(input("Numarul de piese create aleatoru este: "))
            except:
                raise ValueError("Nu este un intreg cel introdus")
            service.Generate(numar)
        except Exception as e:
            print("Eroare: ", e)
            continue