numeros = [[numero, numero**2] for numero in range(10)]
flat = [y for x in numeros for y in x] # para cada x 
print(numeros)
print(flat)