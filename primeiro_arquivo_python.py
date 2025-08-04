print('-------INÍCIO-------')

estou_com_fome = input('Você está com fome? (Digite "s" para "sim" e "n" para "não"): ') == 's'
tenho_comida = input('Tem comida em casa? (Digite "s" para "sim" e "n" para "não"): ') == 's'

if estou_com_fome and not tenho_comida:
    print('Ir ao mercado')
    print('Voltar para casa')
    print('Preparar uma refeição')
    print('Comer a comida')

elif estou_com_fome and tenho_comida:
    print('Preparar uma refeição')
    print('Comer a comida')
else:
    print('\n-------FIM-------')
