def search(word, char): ##Index içinde karakter arama
    flag = 0
    for idx, i in enumerate(word):
        if i == char and flag == 1: ##Bulmak istediğimiz char ın sayısı
            return idx
        if i == char:
            flag += 1
    return False
sonuc = search('Hakan', 'a')
print(sonuc)

print('-----------------------------')

for a in enumerate('hakan'):
    print(a)

print('-----------------------------')

def no_symbol(text, banned):
    for i in text:
        if i in banned:
            return False
    return True
cikti = no_symbol('Hakan', 'kcs')

print(cikti)

print('-----------------------------')

def no_e(word, banned):
    for i in word:
        if i in banned:
            return False
    return True
no_e('dbhcvfkjdh', 'e')