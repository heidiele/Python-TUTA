def laske_kustannus(kappalehinta, maara):
    kokonaiskustannus = kappalehinta * maara
    return kokonaiskustannus


#Pääohjelma
hinta = float(input("Anna tuotteen valmistuskustannus (€): "))
maara = int(input("Kuinka monta tuotetta valmistetaan? "))

tulos = laske_kustannus(hinta, maara)

print("Valmistuksen kokonaiskustannus:", tulos, "€")