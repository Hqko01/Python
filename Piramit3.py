def a(x):
    b = " "
    p = "*"
    for l in range(x):
        pass
    
    for i in range(x):
        print((l - i) * b + p + (2 * (i * p)))

    for k in range(x):
        print(b * k + p + p * ( 2 * (i - k)))
a(20)
