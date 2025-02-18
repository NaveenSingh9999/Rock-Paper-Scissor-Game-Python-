import random
import os

game_name = "Rock Paper Scissor Game"
print("(log) Game rps started at display !")

game_exit = False
print(game_name)
print('')
rps = ['Rock','Paper','Scissor']
bot_sign = random.choice(rps)
print('Welcome To Rock Paper Scisoor Game By NaveenSingh9990 ! Play And Enjoy')
print('')
print('Choose Your Action = Rock , Paper And Scissor And For Exit Type Exit!')
print('')

while game_exit is False:

    # Now For Logic

    user_input = input('Enter : ')
    if user_input == 'Rock':
        print("Bot's Action = " + bot_sign)
        if bot_sign == 'Rock':
            print('')
            print('Game Tie!')
        if bot_sign == 'Scissor':
            print('')
            print('You Won!')
        if bot_sign == 'Paper':
            print('')
            print('You Failed!')
    
    elif user_input == 'Paper':
        print("Bot's Action = " + bot_sign)
        if bot_sign == 'Paper':
            print('')
            print('Game Tie!')
        if bot_sign == 'Scissor':
            print('')
            print('You Failed!')
        if bot_sign == 'Rock':
            print('')
            print('You Won!')

    elif user_input == 'Scissor':
        print("Bot's Action = " + bot_sign)
        if bot_sign == 'Scissor':
            print('')
            print('Game Tie!')
        if bot_sign == 'Rock':
            print('')
            print('You Failed!')
        if bot_sign == 'Paper':
            print('')
            print('You Won!')
        
    elif user_input == 'Exit':
        game_exit = True

    else:
        print('Wrong Action!')

        


