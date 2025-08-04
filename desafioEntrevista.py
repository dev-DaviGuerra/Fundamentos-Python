nome = str(input(f"Olá, qual o seu nome\nDigite aqui: "))
idade = int(input(f"Qual a sua idade?\nDigite aqui: "))
quantidade_de_letras = len(nome)
idade_futuro = idade + 5

print('-' * 10)
print(f"Olá {nome}, o seu nome tem {quantidade_de_letras} letras\nDaqui 5 anos você terá {idade_futuro} anos.")
print('-' * 10)
