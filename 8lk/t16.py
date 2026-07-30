a = 1
b = 1
c = 0
laskuri = 2
kerrat = int(input("Anna luku:"))
print(a)
print(b)
while laskuri < kerrat:
    c = a + b
    print(c)
    a = b
    b = c
    laskuri = laskuri + 1
#ohjelma tulostaa käyttäjän antaman luvun verran fibonaccin lukujonon lukuja.