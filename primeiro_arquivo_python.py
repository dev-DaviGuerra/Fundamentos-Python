tup = (0, 0, 0, 1, 0, 1, 0)
tup.index(1)

tup.count(0)

l1 = [0, 0, 0, 0, 1, 0, 1]

l2 = l1.copy

print(f'L1: {l1}')
print(f'l2: {l2}')

for n in range(5):
    l1.append(n * 2)
print(l1)

l1.append('hello')
print(l1)

valores = [10, 20, 30, -90, -1, 0, 1]
valores_positivos = []

for valor in valores:
    if valor >= 0:
        valores_positivos.append(valor)
print(valores_positivos)

numeros = [1, 2, 3]
numeros.extend([4, 5, 6])
print(numeros)

numeros2 = [1, 2, 3]
novos_numeros = numeros + [4, 5, 6]
print(novos_numeros)

vogais = ['a', 'i', 'o', 'u']
vogais.insert(1, 'e')
print(vogais)

valores_ = [150, 20, 30, 40, 50]

valor_removido = valores_.pop()
print(valor_removido)

valores_.reverse
print(valores_)

valores_.sort()
print(valores_)