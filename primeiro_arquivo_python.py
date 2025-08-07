while True:
    opt = input('Escolha uma opção (1, 2) | "q" para sair: ')
    if opt == 'q':
        break
    elif opt not in ('1', '2'):
        print('Opção inválida! Digite 1 ou 2. ')
        continue
    else:
        print(f'Opção selecionada: {opt}')