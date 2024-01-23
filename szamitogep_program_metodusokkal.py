from Szamitogep import Szamitogep


# def lista_megadasa():
#     peldany1 = Szamitogep("Win", 32)
#     peldany2 = Szamitogep("Mac", 16)
#     peldany3 = Szamitogep("Win", 16)
#
#     szamitogepek = []
#
#     szamitogepek.append(peldany1)
#     szamitogepek.append(peldany2)
#     szamitogepek.append(peldany3)


def lista_megadasa_file():
    f = open("szamitogep.txt", "r", encoding="utf8")
    sorok = f.readlines()
    f.close()
    szamitogepek = []
    for i in range(len(sorok)):
        szamitogepek.append(Szamitogep(sorok))

    return szamitogepek


def kiiras(lista):
    for i in range(len(lista)):
        op_r = lista[i].op_r
        ram = lista[i].ram
        print(f"{op_r} ({ram})")

# rövid verzio
# kiiras(lista_megadasa())

# hosszabb verzió

lista = lista_megadasa()
kiiras(lista)

def atlag(lista):
    print("Átlag: ", end="")
    ossz = 0
    for i in range(len(lista)):
        ossz += lista[i].ram
    print(round(ossz / len(lista), 3))


def legtobb(lista):
    print("Legtöbb ram-ot tartalmazó oprendszer: ", end="")
    max_i = 0
    for i in range(len(lista)):
        if lista[max_i].ram < lista[i].ram:
            max_i = i
    print(lista[max_i].op_r)


def megszamlalas(lista):
    print("Hány windows-os gépünk van? ", end="")
    hany = 0
    for i in range(len(lista)):
        if lista[i].op_r == "Win":
            hany += 1
    print(f"{hany} db Windows-os számítógépünk van.")


def eldontes(lista):
    vizsgaltram = 22
    print(f"Van-e {vizsgaltram} GB-nál nagyobb Windows? ", end="")

    van = False
    for i in range(len(lista)):
        if lista[i].ram > vizsgaltram and lista[i].op_r == "Win":
            van = True

    if van:
        print("Van")
    else:
        print("nincs")
