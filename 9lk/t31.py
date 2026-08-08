def laske_sanat(merkkijono):
    sanat = merkkijono.lower().split()

    erilliset_sanat = set(sanat)
    return len(erilliset_sanat)

testi = "tämä on testi"
print(laske_sanat(testi))
