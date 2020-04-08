name = input('Ingresa el nombre el usuario: ')
lastName = input('Ingresa el apellido el usuario: ')
age = input('Ingresa la edad del usuario: ')
email = input('Ingresa el correo el usuario: ')

user = {}

user['name'] = name
user['lastName'] = lastName
user['age'] = age
user['email'] = email

for key, value in user.items():
  print(key,':', value)