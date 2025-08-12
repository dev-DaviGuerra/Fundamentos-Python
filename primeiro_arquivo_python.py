texto = """

Python é uma linguagem de programação de alto nível,[10] interpretada de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991

A linguagem foi projetada com a filosofia de enfatizar a importância do esforço do programador sobre o esforço computacional

Python é uma linguagem de propósito geral de alto nível, multiparadigma, suporta o paradigma orientado a objetos, imperativo, funcional e procedural.

O nome Python teve a sua origem no grupo humorístico britânico Monty Python,[13] criador do programa Monty Python's Flying Circus, embora muitas pessoas façam associação com o réptil do mesmo nome (em português, píton ou pitão)

"""
vogais = ['a', 'e', 'i', 'o', 'u']

for vogal in vogais:
    contador_de_vogal = texto.lower().count(vogal)
    print(f'Há {contador_de_vogal} vezes a vogal "{vogal}"')