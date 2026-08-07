def keraa_nimet():
    lista = []
    while True:
        nimi = input("Syötä nimi (tai välilyönti lopettaaksesi): ")
        if nimi.lower() == ' ':
            break
        lista.append(nimi)
    return lista

print(keraa_nimet())