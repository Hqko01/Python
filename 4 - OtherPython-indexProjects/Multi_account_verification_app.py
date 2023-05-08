a = ['hqkko','yılmaz']
b = ['12','13']


def function():
    y = input('Username: ')
    y = str(y)
    for x in range(len(a)):
        if y == a[x]:
            z = input('Password: ')
            if b[x] == z:
                print('Login Succesful..')
            else:
                print('Something is wrong.')
            break
    else:
        print('Something is wrong.')
function()