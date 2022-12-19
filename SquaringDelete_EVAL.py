x = eval(input())

def remove_squares(x):
    removed = list()
    temp = list()
    for i in x:
        if i**2 in x:
            removed.append(i)
            removed.append(i**2)
    for i in x:
        if i not in removed:
            temp.append(i)
    return temp
print(remove_squares(x))
