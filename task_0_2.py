users = [
    {'admin': False, 'active': True, 'name': 'Andrew'},
    {'admin': True, 'active': True, 'name': 'Bob'},
    {'admin': False, 'active': False, 'name': 'Marley'}
    ]

counter = 1
for user in users:
    prefix = ""
    if user['admin'] and user['active']:
        prefix = "ACTIVE - (ADMIN) "
    elif user['active']:
        prefix = "ACTIVE "
    elif user['admin']:
        prefix = "(ADMIN) "
    print(f"{counter} {prefix}{user['name']}")
    counter +=1