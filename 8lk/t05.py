luku = int(input("Syötä kokonaisluku, 0 lopettaa ohjelman: "))
while luku != 0:
    if luku % 3 == 0:
        print("Luku", luku, " on jaollinen kolmella.")
    else:
        print("Luku", luku, " ei ole jaollinen kolmella.")
    luku = int(input("Syötä kokonaisluku, 0 lopettaa ohjelman: "))
