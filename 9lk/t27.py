import math

def janan_pituus(piste1, piste2):
    x1, y1 = piste1
    x2, y2 = piste2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

piste1 = (1, 2)
piste2 = (4, 6)
print(janan_pituus(piste1, piste2))