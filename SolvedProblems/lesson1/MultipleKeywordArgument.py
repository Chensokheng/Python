# When we use **, we can pass multiple keyword argument.
def save_user(**user):
    print(user)
    print(user['name'])
save_user(id=1,name='John',age=23,state='Alaska')
