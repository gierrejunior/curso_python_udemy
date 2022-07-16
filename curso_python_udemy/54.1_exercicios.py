"""
1_Crie uma função que exibe uma saudação com os parâmetros saudacao e nome
"""

def Saunome(saudacao, nome):
    print(f'{saudacao}, {nome}')



saudacao = input(str('Digite uma saudação: '))
nome = input(str('Digite um nome: '))
Saunome(saudacao, nome)