# iki liste arasında ortaklar

h = ['Hakan','Yılmaz']
Ic = ['Yılmaz']

def common(l1,l2):
    temp = []
    for i in l1:
        if i in l2:
            temp.append(i)
    return temp
sonuc = common(h, Ic)
print(sonuc)

# iki liste arasında ortak olmayanlar

def missedValues(l1,a,b):
    for i in range(a,b):
        if i not in l1:
            print(i)
x = [1,2,3,4,7,8,10]
missedValues(x,1,11)