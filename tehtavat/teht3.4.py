vuosi = int(input("Anna vuosiluku: "))

#Tapa 1
if vuosi % 400 == 0:
    print("Vuosi on karkausvuosi.")
elif vuosi % 100 == 0:
    print("Vuosi ei ole karkausvuosi.")
elif vuosi % 4 == 0:
    print("Vuosi on karkausvuosi.")
else:
    print("Vuosi ei ole karkausvuosi.")

#Tapa 2
if vuosi % 4 == 0 and (vuosi % 100 != 0 or vuosi % 400 == 0):
    print("Vuosi on karkausvuosi.")
else:
    print("Vuosi ei ole karkausvuosi.")

#Tapa 3
if vuosi % 4 == 0:
    if vuosi % 100 == 0:
        if vuosi % 400 == 0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")
    