import sys
from .Game import Game

def play_game():
'''function to play the number guessing game. All input is given via the keyboard'''        
    new_game = Game() # initialize a new game
    print(new_game) # print the status of the game
    
    while new_game.num_guesses < 20 and new_game.state == 1:
        ''' run this loop until the player makes 20 guesses, or guesses the correct number'''
        new_game.make_guess()
        
        if new_game.state == 1:
            print(new_game) # print game status if player hasn't won
        
    if new_game.num_guesses == 20:
        new_game.state = 0
        print("Sorry, you ran out of guesses. The computer picked the number {}.".format(new_game.integer))
        
    print("Would you like to play again? (y/n)") #prompt the user to play a new game

    response = str(input())

    if response == 'y': # if user says y, play game, else exit program
        play_game()
    else:
        print("Bye!")
        sys.exit(0)
    

print("GUESS THE NUMBER BETWEEN 0 AND 1,000 IN 20 GUESSES OR LESS!!\n\n")

print("Would you like to play? (y/n)") # ask the user if they want to play, else exit program
response = str(input())

if response == 'y': # if user says y, play game, else exit program
    play_game()
else:
    print("Bye!")
    sys.exit(0)
