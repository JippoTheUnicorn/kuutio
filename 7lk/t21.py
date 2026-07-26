leveys = float(input("Anna tontin leveys: "))
pituus = float(input("Anna tontin pituus: "))
valinta = input("Haluatko laskea tontin pinta-alan vai piirin? (pinta-ala/piiri): ")
if valinta == "pinta-ala":
    pinta_ala = leveys*pituus
    print("Tontin pinta-ala on", pinta_ala, "neliömetriä.")
elif valinta == "piiri":
    piiri = leveys*2 + pituus*2
    print("Tontin piiri on", piiri, "metriä.")