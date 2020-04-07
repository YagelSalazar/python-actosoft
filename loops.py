# For

for i in range(5): #Empieza en 0 y termina en 5
  # for(var i = 0; i < 5; i++)
  print('Hola usuario', i)

print('===============================')
print('Tabla del 4')
for i in range(1, 10): #Empieza en 1 y termina en 10
  # for(var i = 0; i < 10; i++)
  # Tabla del 4
  print(f'4 x {i} = {4*i}')

print('===============================')
print('Numeros pares hasta el 50')
for i in range(0, 52, 2):
  print(i)


print('===============================')
print("Lista de egresados")
persons = ["Arturo", "David", "Topi", "Martin"]

for person in persons:
  print('Ing.', person)

print('===============================')
print('Estudiantes y sus calificaciones')
students = [
  ['Martin', [10, 10, 10]],
  ['Arturo', [7, 8, 9]],
  ['Chocha', [5, 10, 3]],
  ['Topa', [10, 8, 7]],
  ['Tablón', [6, 0, 10]],
]

for student in students:
  print('*************************************')
  print('Nombre del alumno:', student[0])
  print('Calificaciones')

  notes = student[1]

  # Acceder a cada una de las calificaciones de cada estudiante
  # Mostrar cada una
  # Obtener el promedio
  # Si su promedio es mayor que 6, imprimir en la consola 'APROBADO', sino, imprimir 'REPROBADO'
  # sum() Toma una lista de números y hace la suma de todos

  for i, note in enumerate(notes): #enumerate() permite traer el valor y el index de el elemento de una lista
    print(f'Calificación #{i + 1}: {note}')
  
  average = sum(notes)/len(notes)
  # Operador Ternario if else
  # print('PROMEDIO:', average)
  # if average > 6:
  #   print('APROBADO')
  # else:
  #   print('REPROBADO')
  print(f'PROMEDIO: {average:.2f} - {"APROBADO" if average > 6 else "REPROBADO"}')

print("===============================")
print("USANDO EL WHILE")

# Script to greet people. The program will stop when the user says S, if the option entered for the user is invalid, we have a nested while.
opt = 0
while opt != 'S':
  name = input("Por tu nombre pa saludarte, compa: ")
  print("Hola!", name)
  exit = input("Quieres salirte alv? (S/N): ")
  while exit != "S" and exit != "N":
    print("No mames, ingresa una opción válida")
    exit = input("Quieres salirte alv? (S/N): ")
  opt = exit
print("Gracias por dejame saludaaarte")

print('Vamos a la iglesia')
print('Me das tu diezmo?')

acum = 0
payments = 0

while payments < 10:
  pay = float(input('Ingresa tu diezmo a la iglesia: '))
  acum += pay
  payments += 1
print(f'Total de lo que le has pagado a la Iglesia: {acum:.2f}')


newAc = 0

for 1 in range(0, 10):
  pay = float(input('Ingresa tu diezmo a la iglesia: '))
  payments += newAc
print(f'Total de lo que le has pagado a la Iglesia: {newAc:.2f}')