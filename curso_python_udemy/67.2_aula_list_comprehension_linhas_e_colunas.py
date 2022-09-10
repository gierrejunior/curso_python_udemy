#FOR ANINHADO
"""
for x in range(1, 11): # linhas de 1 a 10
    for y in range(1, 6): # colunas de 1 a 5
        print(x,y)
"""

#FOR ANINHADO COM LIST COMPREHENSION

linhas_e_colunas = [
    (x,y) # como não tem uma variavel x,y cria-se dentro do list comprehension
    if y != 2 else (x * 1000, y *1000) # Se o y não for 2 o x e o y serão multiplicado por 1000
    for x in range(1,11)
    for y in range(1,6)
    if x != 2 # só mostra os vlaores onde x != 2
]

print(linhas_e_colunas)