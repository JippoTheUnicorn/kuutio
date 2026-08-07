import math

def kolmion_pinta_ala(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))
    return ala

print(kolmion_pinta_ala(3, 4, 5))