valores = list(range(10))

maiores_que_cinco = []

for valor in valores:
    if valor > 5:
        maiores_que_cinco.append(valor)

resultado = [
    valor + 10
    for valor in valores 
    if valor > 5
]

print(resultado)
print(valores)