luku = 1
viitoset = 0

print("Syötä kokonaislukuja väliltä 1-5. Lopeta syöttämällä 0.")

while luku != 0:
    luku = int(input("Syötä kokonaisluku: "))
    if luku == 5:
        viitoset =  viitoset + 1

print("Syöttettyjen viitosien määrä oli: ", viitoset)