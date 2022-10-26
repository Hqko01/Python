def Piramit(x):
    star = "*"
    for i in range(1, x, 1):
        print(star * i)
    for k in range(1, x, 1):
        print(star * (i - k))
Piramit(20)
