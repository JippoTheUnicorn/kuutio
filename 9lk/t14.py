def suurin_luku(lista):
    suurin = lista[0]
    for luku in lista:
        if luku > suurin:
            suurin = luku
    return suurin

testi = [5, 10, 3, 8, 2]
print(suurin_luku(testi))