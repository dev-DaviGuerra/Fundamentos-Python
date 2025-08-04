numero_certo = 3
descobriu = False

if not descobriu: 
    chute = int(input('Digite o número: '))
    if chute > numero_certo:
        print('O número que você escolheu é maior que o número sorteado')
    elif chute < numero_certo:
        print('O número que você escolheu é menor que o número sorteado')
    else:
        print('Descobriu o número')
        descobriu = True

if not descobriu: 
    chute = int(input('Digite o número: '))
    if chute > numero_certo:
        print('O número que você escolheu é maior que o número sorteado')
    elif chute < numero_certo:
        print('O número que você escolheu é menor que o número sorteado')
    else:
        print('Descobriu o número')
        descobriu = True

if not descobriu: 
    chute = int(input('Digite o número: '))
    if chute > numero_certo:
        print('O número que você escolheu é maior que o número sorteado')
    elif chute < numero_certo:
        print('O número que você escolheu é menor que o número sorteado')
    else:
        print('Descobriu o número')
        descobriu = True


if descobriu:
    print('Parabéns, você ganhou!')
else:
    print(f'Que pena, você perdeu! O número secreto era {numero_certo}')