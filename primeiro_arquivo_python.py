print('-------INÍCIO-------')
usuario_certo = 'Davi'
senha_certa = 'senhaSecreta'

usuario = input('Digite o usuário: ') == usuario_certo
senha = input('Digite a senha: ') == senha_certa

if usuario and senha:
    print('Sucesso')
elif usuario and not senha:
    print('Senha incorreta, tente novamente')
elif not usuario and senha:
    print('Usuário incorreto, tente novamente')
else:
    print('Usuário e senha incorretos, tente novamente')
print('\n-------FIM-------')
