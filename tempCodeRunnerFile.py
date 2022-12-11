from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Escolha sua opção:
        [0] Pedra
        [1] Papel
        [2] Tesoura''')
jogador = int(input('Qual a sua jogada? '))
if jogador != 0 and jogador != 1 and jogador != 2:
    print('JOGADA INVÁLIDA!!! \nJogue novamente')
print('PEDRA')
sleep(1)
print('PAPEL')
sleep(1)
print('TESOURA')
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0:
    if jogador == 0:
        print('EMPATE!!!')
    elif jogador == 1:
        print('VOCÊ VENCEU!!!')
    elif jogador == 2:
        print('VOCÊ PERDEU!!!')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1:
    if jogador == 0:
        print('VOCÊ PERDEU!!!')
    elif jogador == 1:
        print('EMPATE!!!')
    elif jogador == 2:
        print('VOCÊ VENCEU!!!')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2:
    if jogador == 0:
        print('VOCÊ VENCEU')
    elif jogador == 1:
        print('VOCÊ PERDEU')
    elif jogador == 2:
        print('EMPATE!!!')
    else:
        print('JOGADA INVÁLIDA')
