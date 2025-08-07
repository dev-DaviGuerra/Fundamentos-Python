valores1 = [2, 4, 6, 8]
valores2 = [1, 2, 3, 4]

for valor1 in valores1:
    for valor2 in valores2:
        if valor1 == valor2:
            print(f'O seguinte valor aparece nas duas listas:{valor1}')

print('-' * 50)

elemento_em_comum = False

for valor1 in valores1:
    if elemento_em_comum == True:
        break
    for valor2 in valores2:
        if valor1 == valor2: 
            elemento_em_comum = True
            break

if elemento_em_comum == True:
    print(f'Tem elemento em comum entre as listas {valores1} e {valores2}')
else:
    print(f'Não tem nenhum elemento em comum entre as listas {valores1} e {valores2}')
            
        