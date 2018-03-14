user = {'admin': False, 'active': True, 'name': 'Andrew'}


if user['admin'] and user['active']:
    print(f"ACTIVE - (ADMIN) {user['name']}")
elif user['active']:
    print(f"ACTIVE {user['name']}")
elif user['admin']:
    print(f"(ADMIN) {user['name']}")
else:
    print(user['name'])
