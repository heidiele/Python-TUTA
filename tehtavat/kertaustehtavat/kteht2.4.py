hinnasto = {
    "omena": 1.5,
    "banaani": 2.0,
    "appelsiini": 1.8,
    "päärynä": 2.5
}

yhteishinta = 0

while True:
    hedelma = input("Anna hedelmän nimi: ")

    if hedelma == "":
        break

    if hedelma in hinnasto:
        hinta = hinnasto[hedelma]
        print("Hinta:", hinta, "€")
        yhteishinta = yhteishinta + hinta

    else:
        print("Hedelmää ei löydy hinnastosta.")
        vastaus = input("Haluatko lisätä hedelmän? (Kyllä/Ei): ")

        if vastaus == "Kyllä":
            hinta = float(input("Anna hedelmän hinta: "))
            hinnasto[hedelma] = hinta
            yhteishinta = yhteishinta + hinta

print("Yhteishinta:", yhteishinta, "€")

print("Päivitetty hinnasto:")
for hedelma in hinnasto:
    print(hedelma, ":", hinnasto[hedelma], "€")

