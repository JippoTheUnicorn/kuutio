luku = int(input("Anna positiivinen kokonaisluku: "))
kertoma = 1
for k in range(1, luku + 1):
    kertoma *= k
print("Kokonaisluvun", luku, "kertoma on", kertoma)