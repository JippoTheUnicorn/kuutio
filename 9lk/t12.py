def maksimi(luku1, luku2, luku3):
    if luku1 > luku2 and luku1 > luku3:
        return luku1
    elif luku2 > luku1 and luku2 > luku3:
        return luku2
    else:
        return luku3

print("Maksimi on", maksimi(5, 10, 3))
print("Maksimi on", maksimi(15, 10, 3))