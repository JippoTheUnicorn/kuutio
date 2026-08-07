def kysely():
    nimi = input("Anna nimesi: ")
    ika = int(input("Anna ikäsi: "))
    tiedot = [nimi, ika]
    return tiedot

def tulostus(tiedot):
    print("Nimesi on", tiedot[0])
    print("Ikäsi on", tiedot[1])

def main():
    kayttajan_tiedot = kysely()
    tulostus(kayttajan_tiedot)

main()