calificacion = int(input('ingresa calificacion: '))

if calificacion >= 7:
  print('ya pasaste')
elif calificacion >= 5 and calificacion < 7:
  print('apenas y pasaste')
else:
  print('ya ni vengas')