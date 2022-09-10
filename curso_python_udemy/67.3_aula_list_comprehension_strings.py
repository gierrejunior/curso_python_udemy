string = "Gierre Junior"

nova_string = [letra for letra in string]
join_string = ''.join([letra for letra in string])

numero_de_letras = 1
fateamento = '.'.join([
    string[indice:indice + numero_de_letras]
    for indice in range(0, len(string),numero_de_letras)
])

print(nova_string)
print(join_string)
print(fateamento)