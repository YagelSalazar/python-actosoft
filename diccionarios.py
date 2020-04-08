user = {
  'first_name': 'Yagel',
  'last_name': 'Salazar',
  'age': 21,
  'birth-date': '1998-05-14'
}

print(user['first_name'])
print('first_name' in user)
print(user.get('country', 'Mexico'))

#ADD / update

user['email'] = 'yagels.xd@gmail.com'

#DELETE
del user['email']

profile = {'RFC': 'yfuyfutf'}

user.update(profile)

for key, value in user.items():
  print('key:', value)
  print('value:', value)