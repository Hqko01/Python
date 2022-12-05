def tam_tersi(str1, str2):
    for i in range(len(str1)):
        if str1[i] != str2[len(str2) -i - 1]:
            return False
    return True
    
in1 = input()
in2 = input()

sonuc = tam_tersi(in1, in2)
print(sonuc)
