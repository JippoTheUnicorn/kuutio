def luvut_listalle():
    lista = []
    print("Syötä lukuja lisstalle. Tyhjä rivi lopettaa.")
    while True:
        syote = input("Anna luku: ")
        if syote == "":
            break
        lista.append(float(syote))
    return lista

def keskiarvo(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista)

def mediaani(lista):
    if not lista:
        return 0
    jarjestetty = sorted(lista)
    n = len(jarjestetty)
    keskikohta = n // 2

    if n %  2 == 0:
        return (jarjestetty[keskikohta - 1] + jarjestetty[keskikohta])
    else:
        return jarjestetty[keskikohta]

def moodi(lista):
    if not lista:
        return None
    yleisin_luku = lista[0]
    suurin_maara = 0

    for luku in set(lista):
        maara = lista.count(luku)
        if maara > suurin_maara:
            suurin_maara = maara
            yleisin_luku = luku

    return yleisin_luku

testilista = [1, 1, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 6]

print(testilista)
print(keskiarvo(testilista))
print(mediaani(testilista))
print(moodi(testilista))