def kertoma(luku):
    if luku == 0:
        return 0
    else:
        return luku * kertoma(luku - 1)

testi = int(input("Anna luku: "))
print(kertoma(testi))