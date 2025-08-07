capitais = {
    'Brasil': 'Brasília',
    'França': 'Paris',
    'Japão': 'Tóquio',
    'Espanha': 'Madrid'
}

print(capitais['Japão'])

capitais['Inglaterra'] = 'Londres'
print(capitais)

del capitais['Inglaterra']
print(capitais)

capitais['Alemanha'] = 'Berlim'

for pais in capitais:
    capital = capitais[pais]
    print(f'A capital de {pais} é {capital}')

print('-' * 100)

d = dict()

d[10] = 'abc'
d['CHAVE'] = 5
d[3.15] = True

for k in d:
    v = d[k]
    print(f'O valor da chave {k} é {v}')

print('-' * 100)

dados = {
    'João': 11111111,
    'Pedro': 22222222,
    'Davi': 333333333
}

for nomes in dados:
    cpf = dados[nomes]
    print(f'O cpf do {nomes} é {cpf}')