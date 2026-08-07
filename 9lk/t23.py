def tarkista_jaollisuus(n):
    jaollinen = []
    for i in range(2, n + 1):
        if n % i == 0:
            jaollinen.append(i)
    return jaollinen

print(tarkista_jaollisuus(24))
print(tarkista_jaollisuus(36))