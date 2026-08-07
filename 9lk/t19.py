def arvauspeli():
    print("Tervetuloa arvauspeliin! Valitse luku väliltä 1-100.")
    print("Vastaa ohjelman arvauksiin seuraavasti:")
    print(" 'p' jos arvaus on liian pieni")
    print(" 's' jos arvaus on liian suuri")
    print(" 'o' jos arvaus on oikein")

    alaraja = 1
    ylaraja = 100
    arvaukset = 0

    while alaraja <= ylaraja:
        arvaus = (alaraja + ylaraja) // 2
        arvaukset += 1

        vastaus = input(f"Onko {arvaus} oikein (o), liian pieni (p) vai liian suuri (s)? ")
        if vastaus == 'o':
            print(f"Arvasin oikein! Luku oli {arvaus}.")
            print(f"Arvasin luvun {arvaukset} arvauksessa.")
            return
        elif vastaus == 'p':
            alaraja = arvaus + 1
        elif vastaus == 's':
            ylaraja = arvaus - 1

arvauspeli()