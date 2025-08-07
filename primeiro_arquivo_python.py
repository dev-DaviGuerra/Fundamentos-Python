sequencia = [1, 2, 3, 4, 5]
soma = 0
for numero in sequencia:
    soma += numero
    media = soma / len(sequencia)
print(f'A soma da sequência {sequencia} é: {soma}')
print(f'A média da sequência é: {media}')

print('\n\n\n')


numeros = [1, 2, 3, 4, 5, 6, -10]
maximo = sequencia[0]
for numero in numeros:
    if numero > maximo:
        maximo = numero

print(f'O maior número da sequência é: {maximo}')

print('\n\n\n')


palavras = ['time', 'futebol', 'camisa', 'numero', 'juiz', 'gol']

for palavra in palavras:
    if len(palavra) >= 5:
        print(f'Palavra com 5 ou mais caracteres da lista: {palavra}')