from time import gmtime, strftime
timeData = "-----ISTINYE Bank------ \n--" + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + "-- \n-----------------------" #zaman verisini kayıt ediyorum

# Burada global bir kod yaziyorum o yüzden kullanici ve degerlerini array olarak kayit ediyorum
# Mesela ahmet array da 0. yerde diğer arraylar da 0. degerler Ahmet`in 
# Disaridan kullanici ve verileri eklense hic bir sorun olmadan calisacaktir
def welcome():
    Users = ['Ahmet', 'Zeynep'] # kullanıcılar
    UsersPassword = ['1234','4321'] # kullanıcıların şifresi
    UsersMoneys = [100, 2500] # kullanicilarin parasi
    print('--Welcome To ISTINYE Bank (v.0.1)--')

    def logQuery():
        signQuery = input('1.Login\n2.Exit\n>>> ') #giris sorgusuna alıyorum
        signQuery = str(signQuery) #giris sorgusundan gelen cevabı string olarak kayitediyorum
        if signQuery == '1':

            def Login():
                userNameQuery = input('Username: ') # giris bilgilerini isteyip string olarak kayit ettim
                userNameQuery = str(userNameQuery)
                for x in range(len(Users)):
                    if userNameQuery == Users[x]:
                        userPasswordQuery = input('Password: ')# giris bilgilerini isteyip string olarak kayit ettim
                        userPasswordQuery = str(userPasswordQuery)
                        if UsersPassword[x] == userPasswordQuery:

                            def mainMenu():
                                serviceQuery = input('Welcome '+ userNameQuery + '!\nPlease enter the number of the service: \n1. Withraw Money \n2. Deposit Money \n3. Transfer Money \n4. My Account Information \n5. Logout \n>>>') # karsiliyorum ve servis sorgusunu baslatiyorum
                                serviceQuery = str(serviceQuery)

                                if serviceQuery == '1':
                                    serviceOne = input('Please enter the amount you want to withdraw: ') #Withdraw miktarini isteyip int değer olarak kayit ettim
                                    serviceOne = int(serviceOne)
                                    if serviceOne > UsersMoneys[x]: # cekme miktari cüzdaninda mevcut olmadigini bildiriyorum
                                        print('You don`t hane ' + str(serviceOne) + ' TL in your account \nGoing back to main menu..')
                                        mainMenu() # Main menu`ye dönüyorum

                                    elif serviceOne <= UsersMoneys[x]: # cekme islemini gerceklestirip yeni cüzdan miktari ile güncelliyorum
                                        print(str(serviceOne) + ' TL withdraw from your account \nGoing back to main menu..')
                                        UsersMoneys[x] = UsersMoneys[x] - serviceOne
                                        mainMenu() # Main menu`ye dönüyorum

                                elif serviceQuery == '2':
                                    serviceTwo = input('Please enter the amount you want to drop: ') # yatirmak istediği miktari soruyorum ve int olarak kayit ediyorum
                                    serviceTwo = int(serviceTwo)
                                    print(str(serviceTwo) + ' TL added to your account \nGoing back to main menu..') # yatirma işleminin gerceklestigini bildirip cüzdanini güncelliyorum
                                    UsersMoneys[x] = UsersMoneys[x] + serviceTwo
                                    mainMenu() # Main menu`ye dönüyorum

                                elif serviceQuery == '3':

                                    def transferUser():
                                        for u in range(len(Users)): # Transferin yapilacagi kullaniciyi sectirtiyorum ve serviceThreeUser`e int olarak kayit ediyorum
                                            print(str(u) + '. ' + Users[u])

                                        serviceThreeUser = input('>>>')
                                        serviceThreeUser = int(serviceThreeUser)
                                        if Users[serviceThreeUser] != Users[x]: # Transferin yapilacagi kullanici ile giris yapan kullanici ayni kisi degilse isleme devam ettiriyorum

                                            def transfer():
                                                serviceThree = input('Please enter the amount you want to transfer: ') # Gönderilecek miktarı girdirip int olarak kayıt ettım
                                                serviceThree = int(serviceThree)

                                                if serviceThree > UsersMoneys[x]: # transfer miktari cüzdan`dan fazla ise
                                                    print('Sorry! You don’t have enough money to complete this transaction')
                                                    transferError = input('1. Go bacnk to main menu \n2. Transfer again \n>>>') # Transfer basarisiz oldu ne yapmak istedigini soruyorum
                                                    transferError = str(transferError)
                                                    if transferError == '1':
                                                        mainMenu()
                                                    elif transferError == '2':
                                                        transfer()

                                                elif serviceThree < UsersMoneys[x]: # transfer miktari cüzdan`dan az ise
                                                    print('Transfer successful')
                                                    UsersMoneys[x] = UsersMoneys[x] - serviceThree
                                                    UsersMoneys[serviceThreeUser] = UsersMoneys[serviceThreeUser] + serviceThree
                                            transfer()

                                        elif Users[serviceThreeUser] == Users[x]: # transfer kendisine yapmaya kalkisilirsa
                                            print('You cannot transfer yourself.')
                                            transferUser()

                                        else:
                                            print('Something is wrong. Try again!') # verilen degerlerden baska bir deger girerse diye 
                                            transferUser()
                                    transferUser()

                                elif serviceQuery == '4':
                                    print(timeData)
                                    print('Your Name: ' + Users[x] + '\nYour Password: ' + UsersPassword[x] + '\nYour Amount (TL): ' + str(UsersMoneys[x]))

                                elif serviceQuery == '5':
                                    print('Logged out') # cikis yapip baslangica gonderiyorum
                                    logQuery()

                                else:
                                    print('Something is wrong. Try again!')
                                    mainMenu() # yanlis sonuc aldigimiz da sorguyu tekrar baslatiyorum
                            mainMenu()

                        else:
                            print('Something is wrong. Try again!')
                            Login() # yanlis sonuc aldigimiz da sorguyu tekrar baslatiyorum
                        break
                else:
                    print('Something is wrong. Try again!')
                    Login() # yanlis sonuc aldıgımız da sorguyu tekrar baslatiyorum
            Login()

        elif signQuery == '2':
            print('Goodbye..')

        else:
            print('Wrong Answer.. Try again!')
            welcome() # 1 veya 2 dışında bir şey girilirse tekrar soruyorum

    logQuery()
welcome()