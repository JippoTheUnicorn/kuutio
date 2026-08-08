def neliojuuri_haarukoimalla(x, tarkkuus=1e-6):
    if x < 0:
        raise ValueError("Negatiivisen luvun neliöjuuri ei ole määritelty.")
    if x == 0:
        return 0.0

    ala = 0.0
    yla = max(1.0, x)

    while (yla - ala) > tarkkuus:
        keskipiste = (ala + yla) / 2
        nelio = keskipiste * keskipiste

        if nelio > x:
            yla = keskipiste
        else:
            ala = keskipiste

    return (ala + yla) / 2

luku = 2
tulos = neliojuuri_haarukoimalla(luku)
print(tulos)
