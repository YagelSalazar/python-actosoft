from random import randint

pc = randit(1,3)

player = int(input('Que arma escoges? (1)Piedra - (2)Papel - (3)Tijera      '))

print('la computadora escoge ', pc)

if player == 1:
  if pc == 1:
    print('Empate')
  elif pc == 2:
    print('Perdiste')
  elif pc == 3:
    print('Ganaste')
elif player == 2:
  if pc == 1:
    print('Ganaste')
  elif pc == 2:
    print('Empate')
  elif pc == 3:
    print('Perdiste')
elif player == 3:
  if pc == 1:
    print('Perdiste')
  elif pc == 2:
    print('Ganaste')
  elif pc == 3:
    print('Empate')