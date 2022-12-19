text = input()

def Q1(txt):
    temp = []
    for i in txt:
        if i not in temp:
            temp.append(i)
    return temp
    
print(Q1(text))
