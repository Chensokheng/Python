admins = ['sokhuong', 'kaka', 'hahaha']
username = input('Enter your name: ')
password = input('Enter your password: ')
if username in admins and username == 'sokhuong' and password == '12345':
    print('Acces granted!')
elif username in admins and username == 'nani' and password == '67890':
    print('Acces granted!')
else:
    print('Acces Denied!')