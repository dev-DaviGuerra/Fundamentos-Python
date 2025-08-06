clientes = [
    ('Yasmim', 'xxx', 'xxx@email.com'),
    ('Davi', 'yyy', 'yyy@email.com')
]

for nome, cpf, email in clientes:
    print(f'Cliente: {nome}\nCPF: {cpf}\nEmail: {email}\n\n')
print('Acabou o loop')