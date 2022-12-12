x = ["Hakan", "Yılmaz"]
y = ['12', '13']
print(x)

x.append('Iclal')  # Array`a eleman ekleme
print(x)

x.insert(0, 'Hqko01')  # Array`a belirlediğimiz bir yere eleman ekleme
print(x)

x.append(y) # Array`a diğer array`ı direkt olarak ekler.
print(x)

x.extend(y) # Array`a diğer seçilen array'daki elemanları ekler.(Direkt olarak array`ı eklemez!)
print(x)

DeletedData = x.pop(2) # Belirlenen öğeyi kaldırır. Ve pop methodumuz silinen veriyi kaydedebilir.
print(x)
print(DeletedData,"<---- 'Silinen veri'")

y.remove('12') # Belirlenen öğeyi siler, kaydetmez.
print(y)

del x[1:3] # Array`da belirlenen öğeden belirlenen diğer elamana kadar siler
print(x)
