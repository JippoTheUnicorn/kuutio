def jarjesta_luvut(lista):
    return sorted(lista)

def tulosta_lista(lista):
    for luku in lista:
        print(luku)

testi = [5, 2, 9, 1, 5, 6]
jarjestetty = jarjesta_luvut(testi)
tulosta_lista(jarjestetty)