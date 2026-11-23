tarina = ""
edellinen_sana = ""

while True:
    sana = input("Anna sana lisättäväksi tarinaan: ")

    if sana == "loppu" or sana == edellinen_sana:
        break

    tarina = tarina + sana + " "
    edellinen_sana = sana

print(tarina)

