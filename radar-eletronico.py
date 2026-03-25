from time import sleep

print('='*45)
print('RADAR ELETRÔNICO'.center(45))
print('='*45)

velocidade = float(input('\nQual é a velocidade atual do carro? '))

print('\nVerificando velocidade...')
sleep(2)

if velocidade > 80:
    print('\nMULTADO!')
    print('Você excedeu o limite de 80 km/h.')
    
    excesso = velocidade - 80
    multa = excesso * 7
    
    print('Velocidade acima do limite: {:.1f} km/h'.format(excesso))
    print('Valor da multa: R$ {:.2f}'.format(multa))
else:
    print('\nTudo certo! Você está dentro do limite.')

print('\nDirija com segurança! Tenha um bom dia!')
print('='*45)