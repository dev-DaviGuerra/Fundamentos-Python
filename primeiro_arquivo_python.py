import math
import datetime
import random
import os
import time

print(math.pi)
print(math.log(16, 2))
#-------------------------------------------------------------------------------
agora = datetime.datetime.now()
anos2000 = datetime.datetime(2000, 1, 1)
print(f'Desde os anos 2000 se passaram: {agora - anos2000}')
#-------------------------------------------------------------------------------
for _ in range(5):
    n = random.randint(1, 5000)
    print(f'Número escolhido: {n}')
nomes = ['Juliano', 'Marcos', 'Paulo']
for _ in range(5):
    nome = random.choice(nomes)
    print(f'Nome escolhido: {nome}')
#-------------------------------------------------------------------------------
print(os.getcwd())
print(os.listdir())
#-------------------------------------------------------------------------------
inicio = time.time()
print('Primeira linha')

time.sleep(3)

print('Segunda linha')
final = time.time()
tempoDeExecucao = final - inicio
print(f'O programa demorou: {tempoDeExecucao:.3f} segundos para ser executado')
print(dir(time))