def pisinsana(lista):
    if not lista:
        return ""

    pisin = lista[0]
    for sana in lista:
        if len(sana) > len(pisin):
            pisin = sana
    return pisin

testi = ["moi", "kissa", "hevonen", "hei"]
print(pisinsana(testi))