def analysoi_tuotanto(tuotantomaarat):
    yhteensa = 0

    for maara in tuotantomaarat:
        yhteensa = yhteensa + maara

    return yhteensa


#Pääohjelma
tuotanto = [120, 150, 90, 180, 160]

tulos = analysoi_tuotanto(tuotanto)
keskiarvo = tulos / len(tuotanto)

print("Tuotantomäärät:", tuotanto)

print("Tuotanto yhteensä:", tulos, "kpl")
print("Keskimääräinen päivätuotanto:", keskiarvo, "kpl")

