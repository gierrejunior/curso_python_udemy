
# NÃO É UMA COPIA E SIM UM APONTAMENTE DE UMA VARIAVEL PRA OUTRA VARIAVEL, ONDE QUANDO UM É ALTERADA, A OUTRA TAMBÉM É
"""
numeros = [1,2,3,4,5]

novos_numeros = numeros # Não está gerando uma cópia, está somente apontando pro mesmo local na memória, qualquer mudança, "afetará" as duas variaveis

novos_numeros[0] = 20
print(numeros) # numeros foi alterado
print(novos_numeros)

"""

# fORMAS DE CRIAR UMA CÓPIA 
"""
numeros = [1,2,3,4,5]

novos_numeros = numeros.copy() # está fazendo uma cópia simples
novos_numeros = [numero for numero in numeros] # outrra forma de fazer uma cópia, usando o lsit comprehension

novos_numeros[0] = 20
print(numeros) # numeros não foi alterado
print(novos_numeros)
"""

numeros = [1,2,3,4,5]

divisao = [numero/2 for numero in numeros] # Divide a lista por 2, sem alterar a lista anterio, pq está criando uma nova lista
multiplicacao = [numero*2 for numero in numeros]
quadrado = [numero**2 for numero in numeros]

print(numeros)
print(divisao)
print(multiplicacao)
print(quadrado)
