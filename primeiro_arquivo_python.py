numero_secreto = 10
descobriu = False

for tentativas in range(3):
    if not descobriu:
        chute = int(input('Digite um número: '))
        if chute < numero_secreto:
            print('Chutou baixo!')
        elif chute > numero_secreto:
            print('Chutou alto!')
        else:
            print('Descobriu!')
            descobriu = True

if descobriu:
    print('Parabéns, você ganhou!')
else:
    print('Que pena, você errou!')