import sys
from .Game import Game

def play_game():        
    new_game = Game()
    print(new_game)
    
    while new_game.num_guesses < 20:
        new_game.make_guess()
        print(new_game)
        
    if new_game.num_guesses == 20:
        print("Sorry, you ran out of guesses. The computer picked {}".format(new_game.integer))
        
    print("Would you like to play again? (y/n)")

    response = str(input())

    if response == 'y':
        play_game()
    else:
        print("Bye!")
        sys.exit(0)
    

print("GUESS THE NUMBER BETWEEN 0 AND 1,000 IN 20 GUESSES OR LESS!!\n\n")

print("Would you like to play? (y/n)")
response = str(input())

if response == 'y':
    play_game()
else:
    print("Bye!")
    sys.exit(0)

