def tarkista_jaollisuus(luku):
    jaollinen = []
    for i in range(2, 9):
        if luku % i == 0:
            jaollinen.append(i)
    return jaollinen

print(tarkista_jaollisuus(24))
print(tarkista_jaollisuus(36))