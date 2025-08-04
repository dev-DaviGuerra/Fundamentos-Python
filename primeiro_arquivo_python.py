idade = int(input("Digite a sua idade: "))

if idade < 18: 
    print('Você tem menos de 18 anos.\nEntão você é menor de idade')
elif idade == 18:
    print('Você tem exatamente 18 anos.\nEntão você é maior de idade')
else:
    print('Você tem mais de 18 anos.\nEntão você é maior de idade')