kirjaimet = ["A", "B", "C", "D", "E"]
for k1 in kirjaimet:
    for k2 in kirjaimet:
        if k1 != k2:
            for k3 in kirjaimet:
                if k3 != k1 and k3 != k2:
                    for k4 in kirjaimet:
                        if k4 != k1 and k4 != k2 and k4 != k3:
                            for k5 in kirjaimet:
                                if k5 != k1 and k5 != k2 and k5 != k3 and k5 != k4:
                                    sana = k1 + k2 + k3 + k4 + k5
                                    print(sana)