print('-------INÍCIO-------')

fome = input('Você está com fome? (Digite "s" para "sim" e "n" para "não"): ')

if fome == 's':
    comida_em_casa = input('Você tem comida em casa? (Digite "s" para "sim" e "n" para "não"): ')
    if comida_em_casa != 's':
        print('Ir ao mercado')
        print('Voltar para casa')
    print('Preparar uma refeição')
    print('Comer a comida')
print('\n-------FIM-------')
