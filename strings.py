# Hola, mundo tiene 11 caracteres
# 


# Indices de caracteres
# string = input('Escribe un mensaje: ')
# primer_letra = string[0]
# longitud = len(string)
# ultima_letra = string[len(string) - 1]
# string[-1]

# print(ultima_letra)


# Slices
mensaje = 'Estoy aprendiendo a programar con Python'
slicito_1 = mensaje[12:]
slicito_2 = mensaje[:21]
slicito_3 = mensaje[6:17]
# print(slicito_1)
# print(slicito_2)
# print(slicito_3)

splited = mensaje.split(" ")
# print(splited)

# print(splited[1])

# Listas
lista = ['palabra', 3, 5.43, True, ['soy', 'otra', 'lista']]
# print(lista[4][1])
# lista_anidada = lista[4]
# lista_anidada[1]
print(lista)

# Quitamos el ultimo elemento
lista.pop()
# nueva_lista = lista.pop()
# print(nueva_lista)
print(lista)

# Agregar un elemento al final
lista.append(False)
print(lista)

lista_string = ['1', '2', '3', '4']
separador = '-'
# join toma una lista de string forzosamente y lo convierte a un string
lista_joineada = separador.join(lista_string)
print(lista_joineada) # 1-2-3-4