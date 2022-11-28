import time

print('Welcome for hqkko banks.')
time.sleep(1)

def inquiry():
    Account_inquiry = input('Do you have a Bank Account?: ')

    if Account_inquiry == 'yes':
        def AccountLogin(Name, Password):
            loginName = input('Account Name: ')
            loginName = str(loginName)
            time.sleep(1)
            loginPassword = input('Account Password: ')
            loginPassword = str(loginPassword)
            time.sleep(2)
            if loginName == Name:
                if loginPassword == Password:
                    print('Logged!')
                else:
                    print('someone it`s wrong')
                    time.sleep(1)
                    ContinueORok = input('Do you want to try again?: ')

                    if ContinueORok == 'yes':
                        AccountLogin('Hakan', '1234')

                    else:
                        print('Goodbye')
            else:
                print('someone it`s wrong')
                time.sleep(1)
                ContinueORok = input('Do you want to try again?: ')
                if ContinueORok == 'yes':
                    AccountLogin('Hakan', '1234')
                    
                else:
                    print('Goodbye')

        AccountLogin ('Hakan', '1234')

    elif Account_inquiry == 'no':
        AccountCreate_inquiry = input('Do you want to create a bank account?: ')
        
        if AccountCreate_inquiry == 'yes':
            AccountCreate_name = input('Account Name: ')
            AccountCreate_name = str(AccountCreate_name)
            AccountCreate_Password = input('Account Password: ')
            AccountCreate_Password = str(AccountCreate_Password)
            time.sleep(1)
            print('Great! you now have a bank account')
            time.sleep(1)
            print('Login to your bank account now')
            time.sleep(1)

            def AccountLogin(Name, Password):
                loginName = input('Account Name: ')
                time.sleep(1)
                loginPassword = input('Account Password: ')
                time.sleep(2)
                if loginName == Name:
                    if loginPassword == Password:
                        print('Logged!')
                    else:
                        print('someone it`s wrong')
                        time.sleep(1)
                        ContinueORok = input('Do you want to try again?: ')
                        if ContinueORok == 'yes':
                            AccountLogin(AccountCreate_name, AccountCreate_Password)
                    
                        else:
                            print('Goodbye')
                else:
                    print('someone it`s wrong')
                    time.sleep(1)
                    ContinueORok = input('Do you want to try again?: ')

                    if ContinueORok == 'yes':
                        AccountLogin(AccountCreate_name, AccountCreate_Password)

                    elif ContinueORok == 'no':
                        print('Goodbye')

            AccountLogin (AccountCreate_name, AccountCreate_Password)
        else:
            print('Goodbye..')
    else: 
        print('yes or no')
        inquiry()
inquiry()
