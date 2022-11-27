import random
from time import sleep
player1 = str(input('ROCK, PAPER or SCISSORS? ')).capitalize()
player2 = random.randint(1,3)

if player2 == 1:
    player2 = "Rock"
elif player2 == 2:
    player2 = 'Paper'
elif player2 == 3:
    player2 = 'Scissors'
    print('-==' * 15)
    print('JO')
    sleep(0.7)
    print('KEN')
    sleep(0.7)
    print('PO!')
    sleep(1)
print('Bot: ', player2)
if player1 == player2:
    print('It´s a tie!')
elif (player1 == 'Rock' and player2 == 'Scissors') or (player1 == 'Paper' and player2 == 'Rock') or (player1 == 'Scissors' and player2 == 'Paper'):
    print('You win!')
else:
    print('You lose!')