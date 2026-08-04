def kertotaulu(luku):
    for i in range(1, 11):
        print(luku, "x", i, "=", luku * i)

luku = int(input("Anna luku (1-10): "))

kertotaulu(luku)