tuntipalkka = float(input("Anna tuntipalkka: "))
tunnit = float(input("Anna tehdyt tunnit: "))
paiva = input("Anna viikonpäivä: ")

if paiva == "sunnuntai":
    palkka = tuntipalkka * tunnit * 2
else:
    palkka = tuntipalkka * tunnit

print("Päiväpalkka:", palkka, "€")