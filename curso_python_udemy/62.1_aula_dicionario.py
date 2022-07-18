clientes ={
    'cliente1' : {
        'nome': 'Gierre',
        'sobrenome' : 'Junior'
    },
    'cliente2' :{
        'nome': 'Uriel',
        'sobrenome': 'Aldrich'
    },
    'cliente3': {
        'nome': 'Erica',
        'sobrenome': 'Caroline'
    }
}

# iterando sobre dicionário dentro de dicionario

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}') #/t da um tab, facilita a leitura



# atribuir o dicionario a outra váriavel não cria um dicionário novo, na verdade as duas variáveis apontam pro mesmo icionário na memória,
# logo quando altera o dicionario em uma váriavel, altera o dicionário em todas as váriaveis que apontam pra ele

d1 = {1 : 'a', 2 : 'b', 3 : 'c'}
v = d1

v[4] = 'd'

print(v)

print(d1) # apesar da alteação ter sido em v, muda o d, pois as variaveis apontam para o mesmo dicionário na memória


# para copiar o dicionário  tem que usar o .copy(), que faz uma cópia rasa

d1 = {1 : 'a', 2 : 'b', 3 : 'c'}
v = d1.copy()

v[1] = 'GR'

print(d1)
print(v)

# Porém por ser umq cópia rasa possui as suas limitações, como por exemplo

d1 = {1 : 'a', 2 : 'b', 3 : 'c', 4 : ['Gierre', 'junior']}
v = d1.copy()

v[4][0] = 'Uriel' #por ser uma cópia rasa, ele acaba alterando o dicionario do d1 também e não o da copia rasa, issoa contece, com listas, dicionários.

print(v)
print(d1)

# para criar uma cópia real e independente é necessário importar a biblioteca copy, é uma biblioteca nativa do python

import copy

d1 = {1 : 'a', 2 : 'b', 3 : 'c', 4 : ['Gierre', 'junior']}
v = copy.deepcopy(d1) # Literalmente uma cópia profunda

v[4][0] = 'Uriel'

print(d1)
print(v)

# é possível fazer cash pra dicionário tambem, porém quem que haver pares, como chaves e valores

lista = [
    ['c1', 1],
    ['c2', 2],
    ['c3', 3],
]

d1 = dict(lista)
print(d1)

#funciona tambem dessas outras formas

lista = (
    ['c1', 1],
    ['c2', 2],
    ['c3', 3],
)

d1 = dict(lista)
print(d1)

# ou

lista = (
    ('c1', 1),
    ('c2', 2),
    ('c3', 3),
)

d1 = dict(lista)
print(d1)

# ou

lista = [
    ('c1', 1),
    ('c2', 2),
    ('c3', 3),
]

d1 = dict(lista)
print(d1)

# Eliminar  conteudo do dicionario, usando POP

d1.pop('c3') # elimina o item pela chave

print(d1)

d1.popitem() #deleta o ultimo item do dicionario, independente do q seja

print(d1)

# Concatenando dicionários

d1 = {
    1 : 2,
    3 : 4,
    5 : 6,
}

d2 = {
    'a' : 'b',
    'c' : 'd',
}

print(d1)
print(d2)

d1.update(d2)
print(d1)
