def PiramiThree(x):
    star = "*"
    space = " "
    for k in range(1, x, 1):
        print(".")

    for i in range(1, x, 1):
        print((space * (i - k)) + (star * i) + (space * i) + (star * i))
PiramiThree(20)
