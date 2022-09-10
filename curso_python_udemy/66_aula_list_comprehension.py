# usar list comprehension é bom ,pois melhora a performance e diminui o número de linhas do código

l1 = [ 1, 2, 3, 4, 5, 6, 7, 8, 9]

ex1 = [variavel for variavel in l1]

print(ex1)

# multiplicando l1 por 2

ex2 = [v *2 for v in l1]

print(ex2)

# criar uma tupla, tipo coordenadas com o l1 

ex3 = [[v, v2] for v in l1 for v2 in range(3)] # Equivale a um for dentro de um for

print(ex3)

# substituindo letras de strings dentro de uma lista

l2 = ['gierre', 'uriel', 'erica']

ex4 = [v.replace('e', '3').upper() for v in l2]

print(ex4)

#inverter ou trocar posições d elista dentro d euma lista

lista = [
    ['chave', 'valor'],
    ['chave2', 'valor2'],
]

ex5 = [[y,x] for  x , y in lista]
print(ex5)
ex5 = dict(ex5) # transforma a lista em dicionário

# usar mais d eum if em list comprehension

l3 = list(range(100)) # cria uma lista de 0 a 99

ex6 = [ v for v in l3 if v % 2 == 0] # cria uma lista com todos os números divisíveis por 2

ex7 = [v for v in l3 if v %3 == 0  if v %8 ==  0]  # cria uma lista com os numeros divisíveis por 3 E por 8

ex8 = [v for v in l3 if v %3 == 0  or v %8 ==  0]  # cria uma lista com os numeros divisíveis por 3 OU por 8

ex9 = [v if v %3 == 0 else 0 for v in l3] # com else, os números que não são divisíveis por 3, são substituídos por 0

ex10 = [v if v %3 == 0 and v%8 == 0 else 0 for v in l3] # com dois ifs e um else

print(ex6)
print(ex7)
print(ex8)
print(ex9)
print(ex10)
