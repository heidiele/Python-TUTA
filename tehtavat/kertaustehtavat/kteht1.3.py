while True:
    print("Tuote valmistettu!")
    vastaus = input("Jatketaanko tuotantoa? ").lower()

    if vastaus == "ei":
        break

print("Tuotanto lopetettu!")