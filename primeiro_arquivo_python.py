letras_minusculas = 'abcdefghijklmnopqrstuvwxyz'
letras_maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
cifra = ''
texto = 'Ola Mundo'
chave = 2

def cifrar_caractere(caractere, seq, chave):
    indice_atual = seq.index(caractere)
    novo_indice = indice_atual + chave
    #Lidar com situação onde indice esta a direita da seq
    while novo_indice >= len(seq):
        novo_indice = novo_indice - len(seq)
    #Lidar com situação onde indice esta a esquerda da seq
    while novo_indice < 0:
        novo_indice = novo_indice + len(seq)
    return seq[novo_indice]


for caractere in texto:
    if caractere in letras_minusculas:
        caractere_cifra = cifrar_caractere(caractere, letras_minusculas, chave)
    elif caractere in letras_maiusculas:
        caractere_cifra = cifrar_caractere(caractere, letras_maiusculas, chave)
    else:
        caractere_cifra = caractere  
    cifra += caractere_cifra

print(cifra)