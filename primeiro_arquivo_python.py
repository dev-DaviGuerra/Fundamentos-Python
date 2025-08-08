x = 4.5
print(x.as_integer_ratio())

y = 38.125
print(y.as_integer_ratio())
print(y.is_integer())

z = 4.0
print(y.is_integer())

palavra = 'Olá Mundo!'
print(palavra.upper())
print(palavra.lower())

arquivo = '2023_01_01_NotaFiscal.docx'
print(arquivo.endswith('.pdf'))
print(arquivo.startswith('2023'))

if arquivo.endswith('pdf') and arquivo.startswith('2023'):
    print(f'PDF de 2023 encontrado: {arquivo}')
else:
    print(f'Este "{arquivo}" NÃO corresponde ao arquivo que estamos procurando')

texto = 'Hoje em dia todo dia é um novo dia. Mais um dia chega. Dia'
print(texto.lower().count('dia'))

seq = 'aaaaaaabaaaaaaaabaaaaaaaab'
print(seq.find('b'))
print(seq.index('b'))

print(seq[seq.find('b'):])

s1 = '435346256234'
print(s1.isdigit())

s2 = 'EIRGNWINfnaefanvuineaiNFUwNUNUununnlapre'
print(s2.isalpha())

s3 = 'Olá 2025 python'
print(s1.isdigit())
print(s2.isalpha())

frase = 'Estou estudando Python!'
print(frase.replace('!' , '?'))

linha = 'Item1;Item2;Item3'
print(linha.split(';'))

nomes = ['Joana', 'Marcelo', 'Paulo']
print('---'.join(nomes))