def sanapeli():
    oikea_sana = input("Pelaaja 1, anna sana: ").strip()

    print("\n" * 50)

    vokaalit = "aeiouyäöAEIOUYÄÖ"
    muokattu_sana = ""
    for kirjain in oikea_sana:
        if kirjain not in vokaalit:
            muokattu_sana += kirjain

    print(f"Pelaaja 2, tässä on sana ilman vokaaleja: {muokattu_sana}")

    yritykset = 3
    while yritykset > 0:
        arvaus = input(f"Arvaa sana, yrityksiä jäljellä: {yritykset} ")

        if arvaus.lower() == oikea_sana.lower():
            print("Arvasit oikein!")
            return
        else:
            print("Arvasit väärin.")
            yritykset -= 1

    print(f"Hävisit pelin. Oikea sana oli: {oikea_sana}")

sanapeli()