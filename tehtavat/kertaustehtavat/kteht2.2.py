def laske_voitto(valmistuskustannus, myyntihinta, maara):
    voitto = (myyntihinta - valmistuskustannus) * maara
    return voitto


#Pääohjelma
kustannus = float(input("Anna tuotteen valmistuskustannus (€): "))
hinta = float(input("Anna tuotteen myyntihinta (€): "))
maara = int(input("Kuinka monta tuotetta myytiin? "))

tulos = laske_voitto(kustannus, hinta, maara)

print(f"Kokonaisvoitto: {tulos:.2f}€")

if tulos < 0:
    print("Tuotanto on tappiollista!")
else:
    print("Tuotanto on kannattavaa!")

