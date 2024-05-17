#rock paper scissors 

import random 
u_score, c_score = 0, 0

def move(value):
    #print('Executed move function.')
    if value == 1: return "rock"
    elif value == 2: return 'paper'
    elif value == 3: return 'scissors'
    

def user_move():
    #print('Executed user_move function.')
    print("Choose your move from below: ")
    print('1. Rock')
    print('2. Paper')
    print('3. Scossors')

    m = int(input())

    return move(m)


def computer_move():
    #print('Executed computer_move function.')
    m = random.randint(1,3)

    return move(m)

def play_game(um, cm):
    global u_score, c_score
    print('Your move: ', um, ' Computer move: ',cm)
    if um == 'rock':
        if cm == 'paper':
            print('You lost! Computer Won!')
            c_score += 1
        elif cm == 'rock':
            print('Tie!')
        elif cm == 'scissors':
            print('You Won! Computer lost')
            u_score += 1

    if um == 'paper':
        if cm == 'rock':
            print('You Won! Computer lost')
            u_score += 1
        elif cm == 'paper':
            print('Tie!')
        elif cm == 'scissors':
            print('You lost! Computer Won!')
            c_score += 1

    if um == 'scissors':
        if cm == 'rock':
            print('You lost! Computer Won!')
            c_score += 1
        elif cm == 'paper':
            print('You Won! Computer lost')
            u_score += 1
        elif cm == 'scissors':
            print('Tie!')

    print('Current Scores: ')
    print('You: ',u_score, '    Computer:', c_score)


play = True

while play:
    print("Do you wanna play Rock-Paper-Scissors?")
    print()
    play = int(input("Enter 1 for YES and 0 for NO: \n"))
    if play:
        a = user_move()
        b = computer_move()
        play_game(a,b)
    print()
#Future tasks - add UI to it using maybe pygame?
        