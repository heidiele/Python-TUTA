def laske_osallistujat(oppilaat):
    kurssi = input("Minkä kurssin osallistujamäärän haluat tarkistaa? ")

    maara = 0

    for oppilas in oppilaat:
        if kurssi in oppilaat[oppilas]:
            maara = maara + 1

    print("Kurssilla", kurssi, "on", maara, "osallistujaa.")


#Pääohjelma
oppilaat = {
    "Matti": ["Python", "Matematiikka"],
    "Maija": ["Python", "Fysiikka"],
    "Pekka": ["Matematiikka", "Fysiikka"]
}

print("Oppilaat ja kurssit:")

for oppilas in oppilaat:
    print(oppilas, ":", oppilaat[oppilas])

#Lisätään uusi oppilas
nimi = input("Anna uuden oppilaan nimi: ")

kurssit = []

while True:
    kurssi = input("Anna kurssi (tyhjä lopettaa): ")

    if kurssi == "":
        break

    kurssit.append(kurssi)

oppilaat[nimi] = kurssit

#Tulostetaan päivitetty sanakirja
print("Päivitetty oppilaslista:")

for oppilas in oppilaat:
    print(oppilas, ":", oppilaat[oppilas])

laske_osallistujat(oppilaat)