username = input('Enter your username: ')
password = input('Enter your password: ')
if not bool(username.strip()):
     print('please enter a username')
else:
    print('you entered:',username)
if not bool(password.strip()):
    print('please enter a password')
else:
    print('you entered:',password)
   