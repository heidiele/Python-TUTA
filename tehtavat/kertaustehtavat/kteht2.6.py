varasto = {
    "Pöytä": 20,
    "Tuoli": 50,
    "Hylly": 15
}

#Tulostetaan alkuperäinen varasto
print("Varastotilanne:")

for tuote in varasto:
    print(tuote + ":", varasto[tuote], "kpl")

#Kysytään lisättävä tuote
tuote = input("Mitä tuotetta lisätään varastoon? ")
maara = int(input("Kuinka monta lisätään? "))

#Päivitetään varasto
if tuote in varasto:
    varasto[tuote] = varasto[tuote] + maara
else:
    varasto[tuote] = maara

#Tulostetaan päivitetty varasto
print("Päivitetty varastotilanne:")

for tuote in varasto:
    print(tuote + ":", varasto[tuote], "kpl")

