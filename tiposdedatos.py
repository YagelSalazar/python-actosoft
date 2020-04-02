#nombre = 'Yagel'
#print('Hola mundo, ' + nombre)
#Operadores aritmeticos y tipos de datos
# = - * / // %
#suma = 5 + 4
#resta = 5 - 4
#multi = 5 * 4
#div = 4 / 2
#divExact = 5 // 2
#print('La suma es igual a ', suma)
#numero = input('ingresa un numero')
#print('el numero ingresado es ', numero)

num1 = float(input('ingresa el primer numero: '))
num2 = float(input('ingresa el segundo numero: '))

totalSuma = num1 + num2
totalMulti = num1 * num2
totalRes = num1 - num2
totalDiv = num1 / num2
totalDivExact = num1 // num2
totalResid = num1 % num2

print('el resultado de la suma es igual a ', '{:0.2f}'.format(totalSuma))
print('el resultado de la multiplicacion es igual a ', '{:0.3f}'.format(totalMulti))
print('el resultado de la resta es igual a ', '{:0.2f}'.format(totalRes))
print('el resultado de la division es igual a ', '{:0.3f}'.format(totalDiv))
print('el resultado de la division exacta es igual a ', '{:0.2f}'.format(totalDivExact))
print('el residuo de la division es igual a ', '{:0.3f}'.format(totalResid))
