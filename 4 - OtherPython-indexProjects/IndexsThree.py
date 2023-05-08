a = "The"
b = "ENGR211"
c = "213090080"
d = "9.12613"

star = "*"

print(a[:2] + len(a[2:]) * star)
print(b[:2] + len(b[2:]) * star)
print(c[:2] + len(c[2:]) * star)
print(d[:2] + len(d[2:]) * star)

print('----------------------')

array = ["The", "ENGR211", "213090080", "9.12613"]

def loop(cnt):
    for i in range(0, len(cnt)):
        print(cnt[i][:2] + len(cnt[i][2:]) * star)
loop(array)

print('----------------------')

def unique_elem(x,y):
    print(x[1])
    print()
    for i in y:
        print(i)
unique_elem("Hello", "Alyo")

print('----------------------')

x = "Istanbul"

y = str(x)[::-1]

print(y)
