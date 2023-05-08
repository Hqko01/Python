from time import gmtime, strftime
timeData = "--- WELCOME TO ISTINYE BANK --- \n     -------------------- \n   /       ISTANBUL       \ \n  |  " + \
    strftime("%Y-%m-%d %H:%M:%S", gmtime()) + \
        "   | \n   \                      / \n     -------------------- " 
        
# girişte kullanmak istediğim karşılama ekranını buraya kaydettim

## Bir çok input verisini string olarak kayıt ettim bunun sebebi girilecek her türlü yanlış işleme karşılık verebilmek.

def bankApp():
    admin = {
        'Name': 'Ibrahim',
        'Password': '1122'
    } # admin bilgileri
    
    Users = ['Ahmed', 'Zeynep', 'Alberto'] # kullanıcı isimleri
    Passwords = ['1234', '4321', '4422'] # kullanıcı şifreleri
    Moneys = [200, 200, 200] # kullanıcı paraları
    withdrawals = {} # kullanıcı withdraw hareketlerinin kayıt edildiği yer
    deposits = {} # kullanıcı deposit hareketlerinin kayıt edildiği yer
    transfers = {} # kullanıcı transfer hareketlerinin kayıt edildiği yer
    
    def queryLE():
        print(timeData)
        queryle = input('1. Login \n2. Exit \n>>> ')
        queryle = str(queryle) # kullanıcıyı karşılıyorum

        if queryle == '1':
            def logMenu():
                queryLogMenu = input('What do you want to login as: \n 1. Admin \n 2. User \n 3. Go Back \n>>> ')
                queryLogMenu = str(queryLogMenu) # giriş türünü soruyorum
                if queryLogMenu == "1":
                    def adminMenu():
                        queryAdminName = input('Admin Name: ') # admin ismini soruyorum
                        queryAdminName = str(queryAdminName)
                        
                        if queryAdminName == admin['Name']:
                            queryAdminPassword = input('Password: ') # admin ismi doğruysa şifresini soruyorum
                            queryAdminPassword = str(queryAdminPassword)
                            
                            if queryAdminPassword == admin['Password']:
                                print(' Welome ' + queryAdminName) # şifreyi doğrulayıp karşılıyorum
                                def adminMainMenu(): # admin mani fonksiyonunu çalıştırıyorum
                                    queryAdminOperation = input('  - - - Admin Menu - - - \nPlease enter a number of the settings operations supported: \n 1. Add User \n 2. Remove User \n 3. Display all Users \n 4. Exit Admin Menu \n>>> ')
                                    queryAdminOperation = str(queryAdminOperation)
                                    
                                    if queryAdminOperation == '1':
                                        newUserName = input('Access Granted \nEnter the new user name: \n>>> ')
                                        newUserName = str(newUserName)
                                        Users.append(newUserName) # yeni kullanıcı ismini kayıt ediyorum
                                        
                                        newUserPassword = input('Enter the new user password: \n>>> ')
                                        newUserPassword = str(newUserPassword)
                                        Passwords.append(newUserPassword) # yeni kullanıcı şifresini kayıt ediyorum
                                        Moneys.append(0)
                                        
                                        print(newUserName + ' was added as an user')
                                        return adminMainMenu()
                                    
                                    elif queryAdminOperation == '2':
                                        userDelete = input('Access Granted \nEnter the user name: \n>>> ')
                                        userDelete = str(userDelete) # girilen kullanıcıyı siliyorum
                                        userDeleteNumber = Users.index(userDelete) # girilen kullanıcı diğer arraylardan silmek için kaçıncı sırada olduğunu buluyorum ona göre diğer bilgileri de kolaylıkla siliyorum
                                        
                                        if userDelete in Users:
                                            Users.remove(userDelete)
                                            Passwords.pop(int(userDeleteNumber))
                                            Moneys.pop(int(userDeleteNumber))
                                            
                                            print(userDelete + ' was removed as an user to ISTINYE BANK')
                                            return adminMainMenu()
                                        
                                        else:
                                            print(userDelete + ' does not exist as an user to ISTINYE BANK')
                                            return adminMainMenu()
                                    
                                    elif queryAdminOperation == '3':
                                        print('Access Granted \nThere are', len(Users), 'users using ISTINYE BANK \n Name & Password: ')
                                        for i, name in enumerate(Users, 1): # döngüyü 1 den başlatıyorum isimleri çekiyorum
                                            print(str(i) +'.' ,name, Passwords[Users.index(name)])
                                        print('------------------------------------')
                                        return adminMainMenu()
                                    
                                    elif queryAdminOperation == '4':
                                        return queryLE()
                                    
                                    else:
                                        print('Wrong Answer.. Try Again!')
                                        return adminMainMenu() # yanlış cevap
                                adminMainMenu()
                                    
                            else:
                                print('Wrong Answer.. Try Again!')
                                return adminMenu()
                                
                        else:
                            print('Wrong Answer.. Try Again!')
                            return adminMenu()
                        
                    adminMenu()
                            
                elif queryLogMenu == "2":
                    def login():
                        queryUsername = input('Username: ') # kullanıcı ismini alıyorum
                        queryUsername = str(queryUsername)
                        
                        withdrawals.update({queryUsername: ''}) # giriş yapan kullanıcıyı diğer kayıt yerlerine kayıt edip içeriğini boş bırakıyorum
                        deposits.update({queryUsername: ''})
                        transfers.update({queryUsername: ''})
                        
                        for x in range(len(Users)):

                            if queryUsername == Users[x]:
                                queryPassword = input('Password: ')
                                queryPassword = str(queryPassword)
                                if queryPassword == Passwords[x]:
                                    def mainMenu():
                                        operationMenu = input(queryUsername + ' Welcome to ISTINYE Bank \n Please enter the number of service \n1. Withdraw Money \n2. Deposit Money \n3. Transfer Money \n4. My Account Information \n5. Logout \n>>> ')
                                        operationMenu = str(operationMenu)
                                        
                                        if operationMenu == '1':
                                            def withdraw():
                                                withdrawBalance = input('Please enter the amount you want to withdraw: ')
                                                withdrawBalance = str(withdrawBalance)
                                                withdrawTime = strftime("%Y-%m-%d %H:%M:%S", gmtime()) # işlem zamanını kayıt ediyorum
                                                if Moneys[x] >= int(withdrawBalance):
                                                    Moneys[x] = Moneys[x] - int(withdrawBalance) # parayı güncelliyorum
                                                    withdrawals[queryUsername] += withdrawTime + ' ' + withdrawBalance + ' TL \n    '  # dict e kayıt ediyorum
                                                    print(withdrawBalance + ' TL withdrawn from your account \nGoing back to main menu..')                                                
                                                    return mainMenu()           
                                                else:
                                                    print('Insufficient balance.. \nTry Again!')
                                                    return withdraw()  
                                            withdraw()
                                        
                                        elif operationMenu == '2':
                                            def deposit():
                                                depositBalance = input('Please enter the amount you want to deposit: ')
                                                depositBalance = str(depositBalance)
                                                depositTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                                                Moneys[x] = Moneys[x] + int(depositBalance)
                                                print(depositBalance + ' TL added to your account \nGoing back to main menu..')
                                                deposits[queryUsername] += depositTime + ' ' + depositBalance + ' TL\n    '
                                                return mainMenu()
                                            deposit()
                                            
                                        elif operationMenu == '3':
                                            def transfer():
                                                transferWho = input('Warning: If you want to abort the transfer please enter abort \nPlease enter the name of the user you want transfer money to: ')
                                                transferWho = str(transferWho) # para transferinin yapılacağı kişiyi seçtiriyorum
                                                
                                                if transferWho == 'abort':
                                                    print('Going back to main menu...')
                                                    return mainMenu()
                                                
                                                elif transferWho == Users[x] or transferWho not in Users:
                                                    print('Transferring to user with the name ' + transferWho + ' is not possible! \nUser does not exist!')
                                                    return transfer() # para transferinin yapılacağı kişide hata varsa bu mesajı veriyorum
                                                
                                                else:
                                                    transferBalance = input('Please enter the amount you want to transfer: ')
                                                    transferBalance = str(transferBalance) # transfer miktarını alıyorum
                                                    
                                                    if Moneys[x] >= int(transferBalance):
                                                        Moneys[x] = Moneys[x] - int(transferBalance) # transfer sonucu kullanıcı parasını güncelliyorum
                                                        
                                                        transferWhoNumber = Users.index(transferWho)
                                                        Moneys[transferWhoNumber] = Moneys[transferWhoNumber] + int(transferBalance) # paranın gönderildiği kişinin parasını güncelliyorum
                                                        transferTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                                                        transfers[queryUsername] += transferTime + ' Transferred to ' + transferWho + ' ' + transferBalance + ' TL\n    '
                                                        print('Money transferred successfully! \nGoing back to main menu...')
                                                        return mainMenu()
                                                    
                                                    else:
                                                        transferError = input('Sorry!, you don`t have the entered amount \n \n1.Go back to main menu \n2.Transfer again \n>>> ')
                                                        transferError = str(transferError) # yeterli parası yoksa ve hatalı bir giriş yaptıysa bu mesajı veriyorum
                                                        
                                                        if transferError == '1':
                                                            return mainMenu()
                                                        
                                                        elif transferError == '2':
                                                            return transfer()
                                                                
                                                        else:
                                                            print('Wrong Answer.. Try Again!')    
                                                            return mainMenu()
                                            transfer()
                                            
                                        elif operationMenu == '4':
                                            print('------- ISTINYE BANK ----- \n----' + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + '---- \n---------------------------- \nYour Name: ' + queryUsername + '\nYour Password: ' + queryPassword + '\nYour Balance Amount (TL): ', Moneys[x] ,'\n----------------------------')
                                            print('User Activities Report: \n \nYour Withdrawals \n    ' + withdrawals[queryUsername])
                                            print('Your Deposits: \n    ' + deposits[queryUsername])
                                            print('Your Transfers: \n    Time Person Amount: \n    ' + transfers[queryUsername])
                                            print('\n---------------------------- \nGoing back to main menu...')
                                            return mainMenu()
                                        
                                        elif operationMenu == '5':
                                            print('logging out..')
                                            return queryLE()
                                        
                                        else:
                                            print('Wrong Answer.. Try Again!')
                                            return mainMenu()
                                        
                                    mainMenu()
                                    break

                                else:
                                    print('Wrong Answer.. Try Again!')
                                    return login()

                        else:
                            print('Wrong Answer.. Try Again!')
                            return login()
                    login()

                elif queryLogMenu == "3":
                    print('Going to back..')
                    return queryLE()

                else:
                    print('Wrong Answer.. Try Again!')
                    return logMenu()
            logMenu()

        elif queryle == '2':
            print('Goodbye..')

        else:
            print('Wrong Answer.. Try Again!')
            return queryLE()
    queryLE()

bankApp()