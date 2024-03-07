import vardata
def login():
    while True:
        userName = input('Enter your username: ')
        if userName in vardata.userData:
            print('Hello ' + userName + ', please enter your password:')
            break
        else:
            print('Sorry, that username is not registered.')
    while True:
        userPass = input('Enter your password: ')
        if userPass == vardata.userData[userName]:
            break
        else:
            print('Sorry, that password is incorrect.')
def register():
    while True:
        newName = input('What should i call you? \n name: ')
        print('Hi,' + newName)
        newPass = input('Please enter your password:')
        if newPass == newName:
            print('Sorry, that password is the same as your name.')
        elif ' ' in newPass:
            print('Password can\'t include blank spaces.')
        else:
            vardata.userData[newName] = newPass
            print('Thanks, '+ newName + ', you are now registered, you can log in now.\n')
            login()
            break