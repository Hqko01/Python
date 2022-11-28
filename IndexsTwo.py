a = input('İsim: ')

print(len(a))

print(a[0])

print(a[len(a) - 1])

print('-----------------------------')

for i in range(0, len(a), 1):
    print(a[i])

print('-----------------------------')

for i in a:
    print(i)

print('-----------------------------')

for i, idx in enumerate(a):
    print(i, idx)

print('-----------------------------')

print(a[2:5])
