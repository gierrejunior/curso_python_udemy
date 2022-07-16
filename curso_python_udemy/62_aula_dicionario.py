# a diferença entre lista e dicionário, é que na lista o python gera automáticamente um ídiice, no dicionário quem programa é que cria esse índice

d1 = {'chave1' : 'valor da chave'}

print(d1)

# adicionando uma nova chave ao dicionário

d1['chave2'] = 'Valor da chave 2'

print(d1['chave2'])

print(d1) # printa toodo o dicionário, com chave e valor

# se atribuir um novo valor a uma chave que ja existe, o vlaor será substituido e a chave recebrrá o valor novo

d1['chave2'] = 'novo valor da chave 2'

print(d1['chave2'])

# utilizar/printar o valor de somente uma chave no dicionário, tudo que vem dentro do colchete é o índice que se deseja acessar

print(d1['chave1'])

# dicionário com chave iguais, a chave receberá o valor da ultima vez que apareceu, pois chaves tem que ser únicas, porém chaves diferentes podem receber o mesmo valor, sme problema

d1 = {'chave': 'valor1', 'chave': 'valor2', 'chave': 'valor3'}

print(d1)

# para chaves, pode ser usado qualquer tipo de valor imutaveis, como números, strings e tuplas, que só possuem valores imutáveis tambem, uplas com listas, não pode

d1 = {
    'str': 'valor',
    123: 'Outro valor',
    (1,2,3,4) : 'Tupla'
}

print(d1[(1,2,3,4)])

# se tentar acessar uma chave que não existe o python da uma exceção e para de funcionar, logo o que ta abaixo dele, não será executado 

#print(d1['naoexiste'])

print('se o print acima não estiver comentado, vai da erro em todos os códigos abaixo dele e essa mensagem  e mais nada abaixo será executada')

# contornando o erro acima:

if 'naoexiste' in d1:
    print(d1['naoexiste'])

print('essa mensagem será executado, pois o print acima só será executado se a chave existir, contornando o erro')

# entrando no if acima

d1['naoexiste'] = 'agora existe'

if 'naoexiste' in d1:
    print(d1['naoexiste'])

print('como a chave agora existe, a execuçaõ entrou no if.')

#com o .get evita-se usar o if acima e mesmo assim não dar erro, poi caso não exista a cahve no dicionário, o get retornará o valor None


print(d1.get('essachavenaoexiste')) #retornará um valor None, pois essa chave não existe

print(d1.get('str')) # retornará o valor a chave, pois essa chave existe


# .update é outra maneir ad eatualizar o  valor de uma chave no dicionário

d1.update({'novachave' : 'criando uma nova chave e um novo valor através do update'}) #essa chave e valor não existia antes, agora existe

print(d1['novachave'])

d1.update({'novachave' : 'alterando o valor de uma chave que já existe através do update'})

print(d1['novachave'])

# apagando a chave e o valor correspondente a ela

del d1['str'] # apagando a chave str e o valor dela

print(d1.get('str')) #não encontrará a chave e retornará como None

# fazendo varredura pelos valores do dicionário e não pelas chaves
print(d1)

print('Tupla' in d1.values()) # se ouver algum valor com 'Tupla' printará na tela True, caso contrario printará False

# usando o len par adescobri quantos pares de chave e  valor há no dicionário

print(len(d1))

# iterando pelo dicionário

for k in d1: # itera somente pelas chaves do dicionário
    print(k)

for v in d1.values(): # itera pelos valosres do dicionário
    print(v)

for kv in d1.items(): #i itera pela chave e valor do dicionario, mas cada chave e seu respectivo valor, formam uma tupla
    print(kv)

# iterando pelo dicionário, por chave e valor sem tupla

for kv in d1.items(): # kv[0] acessa a chave dentro da tupla e o kv[1] acesa o valor dessa cahve dentro da tupla, tirando a chave e o valor da tupla
    print(kv[0], kv[1])

# outra forma de fazer é fazendo o desempacotamento, aí não utiliza os ídices para tirar o cahve e o valor da tupla

for k, v in d1.items():
    print(k, v)
