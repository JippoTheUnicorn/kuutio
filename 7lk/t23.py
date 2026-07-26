ika = int(input("Anna ikäsi: "))

if ika < 13:
    print("Olet lapsi.")
elif ika < 18:
    print("Olet nuori.")
elif ika < 23:
    print("Olet nuori aikuinen.")
else:
    print("Olet aikuinen.")