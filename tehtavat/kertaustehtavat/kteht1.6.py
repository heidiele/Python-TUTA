luvut = []

while True:
    luku = int(input("Anna luku: "))

    if luku == 0:
        break

    luvut.append(luku)

    print("Lisäysjärjestyksessä:", luvut)
    print("Järjestettynä:", sorted(luvut))

    