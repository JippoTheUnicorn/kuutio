def viidella_jaollisuus(luku):
    if luku % 5 == 0:
        return True
    else:
        return False

testi = int(input("Anna luku: "))
tulos = viidella_jaollisuus(testi)
if tulos:
    print(f"{testi} on jaollinen viidellä.")
else:
    print(f"{testi} ei ole jaollinen viidellä.")
