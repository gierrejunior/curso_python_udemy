def funcao_saudacao(saudacao, nome):
    return f'{saudacao}, {nome}'

def bem_vindo(sobrenome):
    return f'Bem vindo Mr.{sobrenome}'

def funcao_mestra(funcao1, funcao2):
    return funcao1, funcao2


executando = funcao_saudacao('oi', 'Gierre'), bem_vindo('Sousa')
for i in executando:
    print(i)
