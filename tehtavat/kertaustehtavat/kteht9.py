tuotteet = []
maarat = []

while True:
    tuote = input("Mitä tuotetta valmistetaan? ")
    maara = int(input("Kuinka monta valmistetaan? "))

    tuotteet.append(tuote)
    maarat.append(maara)

    jatketaan = input("Jatketaanko tuotantoa? ").lower()

    if jatketaan == "ei":
        break


print("\nTuotanto lopetettu!")
print("Valmistetut tuotteet:")

for i in range(len(tuotteet)):
    print(tuotteet[i] + ":", maarat[i], "kpl")