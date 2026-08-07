import random

def arvo_nimi():
    etunimet = ["Matti", "Maija", "Pekka", "Liisa", "Juhani", "Anna"]
    return random.choice(etunimet)

print(arvo_nimi())