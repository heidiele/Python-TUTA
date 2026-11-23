sanat = ["auto", "tuotanto", "tehdas", "työ", "kustannukset"]

maara = 0

for sana in sanat:
    if len(sana) > 5:
        maara = maara + 1

print("Yli viiden kirjaimen sanoja:", maara)

