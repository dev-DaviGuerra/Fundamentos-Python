capitais = {
    'Brasil': 'Brasília',
    'França': 'Paris',
    'Japão': 'Tóquio',
    'Espanha': 'Madrid'
}

print('Brasil' in capitais)
print('Brasília' in capitais)

print('-' * 100)

pais = 'Argentina'

if pais in capitais:
    capital = capitais[pais]
    print(f'A capital para o país {pais} é {capital}')
else:
    print(f'Não há capital registrada para o país {pais}')