def adicionar_final(texto, final="!!!"):
    return texto + final

print(adicionar_final('Olá ', 'Mundo'))


def dividir(n1, n2):
    if n2 == 0:
        return 'Impossível dividir'
    return n1/n2
    
print(dividir(n1=10, n2=5))


def dizer_ola():
    print('Olá!')