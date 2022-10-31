while True:
    def d(x):
        b = " "
        for i in range(0, x, 1):
            print(i, b, end="")
        for a in range(3, -1, -1):
            print(a, b, end="")
        print(" ")
    d(4)
