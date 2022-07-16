"""
2_Crie uma função que receba 3 números como parâmetros e exiba a soma entre eles.
"""

def soma_3_numeros(num1, num2, num3):
    resultado = int(num1) + int(num2) + int(num3)
    print(resultado)



num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')
num3 = input('Digite mais um número: ')

soma_3_numeros(num1, num2, num3)