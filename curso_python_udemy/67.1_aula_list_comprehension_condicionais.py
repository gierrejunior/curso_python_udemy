numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

novos_numeros = [numero for numero in numeros if numero > 5] # Iterar com um filtro usando uma condicional
impares = [numero for numero in numeros if numero % 2 != 0] # Iterar com um filtro usando uma condicional
pares = [numero for numero in numeros if numero % 2 == 0] # Iterar com um filtro usando uma condicional
outro_if = [
    numero if numero != 6 else 600 # operador ternario, vem na frente
    for numero in numeros # iterando uma lista
    if numero % 2 == 0 # condicional comum vem atrás e serve como filtro de valores
    ] 

print(numeros)
print(novos_numeros)
print(impares)
print(pares)
print(outro_if)