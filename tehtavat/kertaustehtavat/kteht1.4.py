from math import sqrt

while True:
    luku = int(input("Anna kokonaisluku: "))

    if luku == 0:
        break
    elif luku < 0:
        print("Virheellinen numero")
    else:
        print("Luvun neliöjuuri:", sqrt(luku))

        