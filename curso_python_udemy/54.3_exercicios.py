"""
3_Crie uma função que receba 2 números. O primeiro é um valor e o segundo é um percentual (ex. 10%). 
Retorne(return) o valor do primeiro número somado do aumento do percentual do mesmo
"""

def soma_percentual(valor, percentual):
    try:
        valor = float(valor)
        percentual = float(percentual)
    except:
        return('valores inválidos')
    valor_percentual = (valor * 100) / percentual
    resultado = valor + percentual
    return resultado



valor = input('Digite um valor: ')
percentual = input('Digite o percentual do valor para ser somado: ')
resultado = soma_percentual(valor, percentual)
print(resultado)