produtos = {
    'banana': 3.60,
    'leite': 4.90,
    'carne': 15.50,
    'pão': 9.00
}
print(produtos)
print(produtos.get('banana', 'Não foi encontrado!'))

print(produtos.setdefault('banana', '100'))
print(produtos.setdefault('arroz', '100'))

print(produtos)

for produto in produtos.keys():
    print(produto)

for valor in produtos.values():
    print(valor)

for k, v in produtos.items():
    print(f'{k} -> {v}')

novos_produtos = {
    'massa': 5.70,
    'banana': 4.40,
}

produtos.update(novos_produtos)
print(produtos)

produtos_copia = produtos.copy()

produtos_copia['morango'] = 3.30

print(produtos)
print(produtos_copia)