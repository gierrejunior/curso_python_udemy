"""
4_Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz, se o parâmetro for divisível por 5, retorne buzz.
Se o parâmetro for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o número enviado
"""

def fizzbuzz(num):
    try:
        num = int(num)
    except:
        return('Digite um valor válido')


    if num % 3 == 0 and num % 5 == 0:
        return ('FizzBuzz')
    if num % 3 == 0:
        return ('Fizz')
    if num % 5 == 0:
        return('Buzz')
    return num


num = input('Digite um número: ')
resultado = fizzbuzz(num)
print(resultado)
