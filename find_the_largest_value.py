list = [1, 2, 3, 4]

x = len(list)
a = 0
for i in range(x):
     if a < list[i]:
         a = list[i]
print(a)
