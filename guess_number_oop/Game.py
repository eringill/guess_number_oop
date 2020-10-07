import random

class Game():
    ''' Game class that keeps track of all game attributes'''
    def __init__(self):
        self.max = 1000 # max integer for computer to choose
        self.min = 0 # minimum integer for computer to choose
        self.integer = random.randint(self.min, self.max) # integer that computer chooses
        self.num_guesses = 0 # number of guesses already made
        self.total_guesses = 20 # number of guesses available
        self.guesses = [] # numbers guessed
        self.state = 1 # state 1 = in play, state 0 = game over
        
    def make_guess(self):
        ''' method to make a guess
        Inputs: integers typed by the user
        Outputs: whether the guess is higher or lower than the actual integer chosen by computer 
        (or the correct integer) and
        the number of guesses left in the game ''' 
        if self.num_guesses < 20:
            
            try:
                guess = int(input("Please guess an integer between {} and {}.\n".format(self.min, self.max)))
            except:
                print ("That guess is not valid. Try again.")
 
            else:
                self.guesses.append(guess) # append guess to list of guesses
                self.num_guesses = len(self.guesses) # number of guesses = length of guesses list
                
                if guess > self.integer:
                    print ("\nThe actual integer is lower than the integer you chose.")
                elif guess < self.integer: 
                    print ("\nThe actual integer is higher than the integer you chose.")
                elif guess == self.integer:
                    self.state = 0
                    print ("\nCongratulations you guessed the number in {} guesses.".format(self.num_guesses))
    
    def __repr__(self):
        ''' returns the number of guesses left and the numbers guessed so far'''
        return "You have {} guesses left out of {} total guesses.\nSo far you have guessed the numbers {}.\n"\
                .format((20 - self.num_guesses), self.total_guesses, self.guesses)
