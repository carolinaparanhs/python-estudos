from random import randint
from time import sleep

print('='*40)
print('JOGO DE ADIVINHAÇÃO'.center(40))
print('='*40)

print('\nO computador pensou em um número entre 0 e 5...')
x = int(input('Tente adivinhar: '))

computador = randint(0, 5)

print('\nProcessando...\n')
sleep(3)

if x == computador:
    print('PARABÉNS! Você acertou!')
else:
    print('Que pena, você errou!')

print(f'O computador pensou em: {computador}')
print(f'Você escolheu: {x}')

print('\n' + '='*40)