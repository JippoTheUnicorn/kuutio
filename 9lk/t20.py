import random

def arvaus_peli():
    salainen = str(random.randint(0, 9999)).zfill(4)
    print("Ohjelma on arponut nelinumeroisen luvun. Yritä arvata se!")

    while True:
        arvaus = input("Arvaa luku: ")

        if len(arvaus) != 4 or not arvaus.isdigit():
            print("Syötä nelinumeroinen luku.")
            continue

        oikea_paikka = 0
        oikea_numero = 0

        # Oikeassa paikassa olevat numerot
        for i in range(4):
            if arvaus[i] == salainen[i]:
                oikea_paikka += 1

        # Oikeat numerot väärässä paikassa
        for i in range(4):
            if arvaus[i] != salainen[i] and arvaus[i] in salainen:
                oikea_numero += 1

        print(f"Oikealla paikalla: {oikea_paikka}, Oikein mutta väärässä paikassa: {oikea_numero}")

        if oikea_paikka == 4:
            print("Onneksi olkoon! Arvasit oikein!")
            break

arvaus_peli()