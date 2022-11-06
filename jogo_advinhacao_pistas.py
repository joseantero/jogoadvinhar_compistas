import random
from random import randint,uniform
from time import sleep
numero = int(random.uniform(0,10))
jogador = ''
print('\033[1:35m^^^^^^^^^^^^^^\033[3:37mJOGO DA ESCOLHA\033[1:35m^^^^^^^^^^^^^^')
sleep(0.5)
cont = 1
while jogador != numero:
    jogador=int(input('\033[0:37mEscolha um número de 0 há 10:'))
    if jogador != numero:
        cont +=1
    if jogador > numero:
        print('digite menos....')
    elif jogador < numero:
        print('digite mais')
print(f'\033[1:31mEu escolhi o número {numero}')
print(f'\033[1:32mVOCE ACERTOU, na {cont}ª tentativa')