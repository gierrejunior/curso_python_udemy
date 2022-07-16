"""
1_ Crie uma função 1 que recebe uma função 2 como parâmetro e retorne o valor da função2 executada.
"""

def funcao1():
    return 'Olá mundo!'

def funcao2(funcao):
    return funcao()

executando = funcao2(funcao1)
print(executando)

