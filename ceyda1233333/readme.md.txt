-Oyun lastMove fonksiyonu ile başlıyor.
-Player1 ve Player2 ile değişken tanımlayıp sorgularımızı sağlayıp veri kayıtlarını yapıyoruz.
-Daha sonrasında bu oyuncuların isimlerinin birbiriyle aynı olmasını ve O karakterini içermemesini sağlayan if döngüsü oluşturdum.

playingFieldQuery()
-İlk if sorgusundan geçtikten sonra playingFieldQuery() fonksiyonu ile karşılanıyor bu fonksiyonda oyun alanının boyutunu sorgulayıp cevaplandırıyoruz.(3x3, 5x5, 7x7) Gibi.

- playingFieldQuery() Fonksiyonunun ilk if sorgusu ile playingField sorgusunun içeriğinin isteğimiz dışında olup olmadığını kontrol ediyoruz. İsteğimiz dışında ise sorguyu tekrar başlatıyoruz.

Ama eğer isteğimizde ise 3 ,5 veya 7 gibi. Ona göre yapıları oluşturup kayıt altına alıyorum.

		    column = ['A','B','C'] # sütun
                    rows = { # sıra
                    "row1": [' ',' ',' '],
                    "row2": [' ',' ',' '],
                    "row3": [' ',' ',' ']
                    }

3x3 Lük bir oyun alanının yapısı. Daha sonrasında oyuncuları oyun kurallarınca gerekli yerlere yerleştirmek için
row alanının merkezine ihtiyacım var.

a = len(rows) / 2  # Merkezini bulup int`e çeviriyorum ki 1.5 u 1 olarak alsın
a = int(a)

Merkezi bulduktan sonra oyuncuları yerleştirmek için

rows['row'+ str(1)][a] = player1 # Oyuncular gerekli yerlere oturtuldu
rows['row'+ str(len(rows))][a] = player2

kodlarını kullanıyorum. 
NOT: rows yapısını daha iyi anlamak için JSON veri tiplerini incelemenizde fayda olacaktır.

-                 # ------Field Çıktısı------
                    print('', end="    ")
                    for f in range(len(column)): # Column dizinindeki verileri teker teker yazdırmak için for                       						   döngüsü kullanıyorum.

                        print(column[f], end="   ") # end="" Komutu ile alt alta ekelenen Column dizinindeki 							      verileri yan yana gelecek şekilde ayarlıyorum. "" lar 							      içindeki boşluk dizindeki veriler arasındaki boşluğu 							      ayarlıyor.
                    for f2 in range(len(column)): # Önceki for döngüsü ile aynı şekilde column dizininin 							    uzunluğunu alıyorum. Ayrı bir şekilde for döndürmemin sebebi 						    önceki eklenen veriler ile burada eklenecek verilerin 							    karışmaması.

                        print('\n  ','-' * int(float(len(column)) * 3.9)) # Çizgi adedini ayarlıyor
                        print(f2 + 1, end=" | ") # Dikey çizgileri gerekli yerlere ekleyen girdi.
                        for f3 in range(len(column)):
                            print(rows['row' + str(f2 + 1)][f3], end=" | ") # İçerideki Hanelerin yanlarına dikey 									      çizgileri ekleyen girdi.
                        print(f2 + 1, end="") # ve bu girdileri de eklerken aşağı inmesini istemiyoruz.
                    print('\n  ','-' * int(float(len(column)) * 3.9)) # Çizgi adedini ayarlıyor
                    print('', end="    ")
                    for f in range(len(column)):
                        print(column[f], end="   ")

Field çıktısı oyun alanımızın çıktısını veren yer.

*daha basiti dümdüz bir şey isterse
print() içinde mesela
print(--- rows['row1'][3]----|) gibi gibi devam eder

-Oyun alanımızı belirledik ve şimdi oyuncularımızın hareket etmesini ve taş eklemesini sağlama zamanı. Bunun için movement() fonksiyonuna gidiyoruz.

-movement() Fonksiyonunda movementPlayer() Fonksiyonu ile oyunu oynayacak oyuncuyu ve konumunu ayarlıyoruz.
startPlayer değişkenine oynayacak oyuncu veriliyor player1 veya player2.


		for x in range(1,len(rows) + 1): 
                    for y in range(len(rows)):
                        if rows['row'+str(x)][y] == startPlayer: # bu for döngüleri ile oyun alanında startPlayer 						     		   de verilen oyuncunun yerini arıyoruz.
                            startPlayerLoc = [] # Oyuncunun yerini bulduktan sonra startPlayerLoc dizinine 							  ekliyoruz. Location = Loc
                            startPlayerLoc.append('row'+str(x))
                            startPlayerLoc.append(column[y])
                            startPlayerLoc.append(x)
                            startPlayerLoc.append(y)
            					   #rows #column #player location # player  #rock type
                            return movementControl(rows, column, startPlayerLoc, startPlayer, 'big')


* #json değişken adı = rows
 #json rows değişkeninin içindeki verilere erişmek için o alanın ismini girmek gerekiyor yani 'row1' 'row2'
şöyle şimdi json veri tipinde rows['row1']
for döngüsünde ['row'] yazıyorum yanına gelecek sayıyı for dan alıyorum ve yanına ekleyebilmem için str ile stringe çeviriyorum.

çünkü o dizin json değil [0] [1] ile erişebiliyoruz içeriğine


- movementControl() Hareket edecek oyuncunun bilgilerini aldık şimdi bu oyuncunun nereye, hangi yöne doğru hareket edebilir bunu bulmalıyız. Bunuda movementControl() fonksiyonu ile sağlıyoruz.

Bu fonksiyonda locs adında dizin tanımlayıp hareket edebileceği konumları giriyoruz.
	locs = ['N','S','E','W','NE','NW','SE','SW']

Daha sonrasında "fullness" adında değişken tanımlayıp 0 değerini veriyoruz. Bunun sebebi oyuncunun etrafını kontrol ettiğimizde mesela;

		if (playerLoc[2] - 1) == 0 or rows['row' + str(playerLoc[2] - 1)][playerLoc[3]] != " ":
                        locs.remove('N')
                        fullness += 1

Bu sorgu ile N konumunun kullanılabilirliğini kontrol ediyoruz. Eğer kullanılamaz ise tanımladığımız fullness değişkenini 1 arttırıyoruz.

Oyuncunun toplamda gidebileceği 8 yol var bu sebepten dolayı fullness 8 e ulaştığında hareket edebileceği bir yeri kalmayan oyuncu kaybetmiş oluyor.

		*  	if player == player1:
                            return lastMoveEnd(player2) # bitirme fonksiyonu
 
*orada boşlugu kalmayan oyuncu player konumuna kayıtlı biz kazananı istediğimiz için orada diğer oyuncuya ihtiyacımız var bunu da if sorgusu ile hallediyoruz.

-Şimdi oyun devam ediyor büyük taş ve küçük taş mevzumuz var.
Bunun için rock değişkenini tanımlamıştık movementControl(rock) fonksiyonuna.

İlk başta taşı big olarak döndürüyoruz bu sayede oyuncu büyük taşını oynadıktan sonra small olarak dönüp küçük taşını oynayacak oyuncu.

				if locs[nl] == newLocation: # newLocation yani oyunucunun büyük taşı için girdiği 							      veriyi kaydettiğimiz yer. Yine bir for döngüsü ile 							      kayıt ettiğimiz locs ve sonrasında çıkarmalar 								      yaptığımız locs dizininin içindeki verileri teker 							      teker for döngüsü ile çekerek newLocation ile 								      sorguluyoruz. Bu for ve if döngülerini "kartezyan" 							      çarpımı olarak düşünebilirsiniz.

							    * Ve else ile değişkenin içindeki veri hareket 								      komutlarında (locs dizininde) yok ise invalid value! 							      cevabı verip sorguyu tekrarlatıyorum.

                                    if newLocation == 'S': # Ve eğer S yönünü istediyse kullanıcı
                                        rows[playerLoc[0]][playerLoc[3]] = ' ' # Eski yeri temizliyoruz
                                        playerLoc[2] += 1 # S dediği için row1 ise row2 olacak o yüzden playerLoc 							    dizinindeki 2. değer 1 arttırılıyor.

                                        playerLoc[0] = 'row' + str(playerLoc[2]) # arttırılan değer playerLoc 											 değişkeninin 0. değeri ile 											 değiştiriliyor.

                                        rows[playerLoc[0]][playerLoc[3]] = player # Oyuncuyu yeni konumuna 										            yerleştiriyoruz.
                                        
                                        # Field Çıktısını Çağırıyorum   		    #rock
                                        return fieldOutput(rows, column, playerLoc, player, 'small')
					
					# Bu sefer field çıktısını çağırırken rock bölümünü small olarak giriyorum 					  çünkü büyük taş oynandı sıra küçük taşta.

- Küçük taşa geldik.


satır 186 *elif rock == 'small':

smallRock değişkeni oluşturup içerisine 1A - 2B gibi verilerin kayıt edileceği input u yazıyorum daha sonrasında sorun yaşanmaması için string olarak kayıt altına alıyorum bu değişkeni.

smallRock değişkenimizin [0] `ncı elementi bizim row sırasındaki konumumuz [1] `nci elementi column sırasındaki konumumuz.

smallRock değişkenini böyl iki parçaya bölüyoruz. Ve;

				for c in range(len(column)):
                                    if column[c] == columnRockLoc:
                                        columnRockLoc = c
                                        
                                        if rows['row' + str(rowRockLoc)][c] == " ":
                                            rows['row' + str(rowRockLoc)][c] = 'O'
                                            return fieldOutput(rows, column, playerLoc, player, 'big')
                                        
                                        elif rowRockLoc > len(rows) or rowRockLoc < 1:
                                            movementControl(rows, column, playerLoc, player, 'small')

                                        else:
                                            movementControl(rows, column, playerLoc, player, 'small')
                                    else:						  #rock
                                        movementControl(rows, column, playerLoc, player, 'small')


Bir for döngüsü ve if else yapısı ile bu parçalara ayırdığımız girdiyi kontrol edip sonuçlandırıyoruz.
*Burada dikkat edilmesi gereken movementControl fonksiyonunun rock kısmını small olarak giriyoruz ki sıra sonraki oyuncuya geçsin.

Oyunumuzun işleyişi bu şekilde kodlamayı anlamak için;

***Fonksiyonları "sırasıyla takip" etmeliyiz ve "kartezyan çarpımı" ile "for if else" arasındaki ilişkiyi anlamamız.

Fonksiyon çalışma sırası;

1- lastMovePlay()
2- playingFieldQuery()
3- movement(rows, column)
4- movementPlayer(startPlayer)
5- movementControl(rows, column, playerLoc, player, rock)

* fieldOutput(rows, column, playerLoc, player, rock) fonksiyonu oyun alanı çıktısını almak içindir fakat buradaki "rock" değişkeni oyuncular arası geçişte önem arz etmektedir.



----Elimden geldiğince anlatmaya çalıştım. Takıldığınız bir yer olursa bana bionluk ve mail üzerinden ulaşabilirsiniz.








