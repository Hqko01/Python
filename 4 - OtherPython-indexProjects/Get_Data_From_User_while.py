menuOne = "Elma"
menuTwo = "Muz"
menuThree = "Karpuz"
menuFour = "Kiraz"
menuFive = "Ananas"

while True:
    y = input("yaz (1 - 5): ")
    y = int(y)

    if 1 <= y <= 5:
        if y == 1:
            print(menuOne)
        elif y == 2:
            print(menuTwo)
        elif y == 3:
            print(menuThree)
        elif y == 4:
            print(menuFour)
        elif y == 5:
            print(menuFive)
        break
    else:
        print("1-5")