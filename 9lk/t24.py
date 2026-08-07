def tarkista_jaollisuus(n):
    jaollinen = []
    for i in range(2, n + 1):
        if n % i == 0:
            jaollinen.append(i)
    return jaollinen

def jaa_tekijoihin(luku):
    tekijat = tarkista_jaollisuus(luku)
    return tekijat

print(jaa_tekijoihin(24))