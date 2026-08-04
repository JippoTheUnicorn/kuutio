def luku_numeroiksi(luku):
    lista = []

    merkkijono = str(luku)
    for merkki in merkkijono:
        lista.append(int(merkki))
    return lista

print(luku_numeroiksi(12345))
    