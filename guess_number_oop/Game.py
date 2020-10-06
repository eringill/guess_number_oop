import random

class Game():
    def __init__(self):
        self.max = 1000
        self.min = 0
        self.integer = random.randint(self.min, self.max)
        self.num_guesses = 0
        self.total_guesses = 20
        self.guesses = []
        
    def make_guess(self):
        if self.num_guesses < 20:
            
            try:
                guess = int(input("Please guess an integer between {} and {}.\n".format(self.min, self.max)))
            except:
                print ("That guess is not valid. Try again.")
 
            else:
                self.guesses.append(guess)
                self.num_guesses = len(self.guesses)
                
                if guess > self.integer:
                    print ("\nThe actual integer is lower than the integer you chose.")
                elif guess < self.integer: 
                    print ("\nThe actual integer is higher than the integer you chose.")
                elif guess == self.integer:
                    print ("\nCongratulations you guessed the number in {} guesses.".format(self.num_guesses))
    
    def __repr__(self):
        return "You have {} guesses left out of {} total guesses.\nSo far you have guessed the numbers {}.\n"\
                .format((20 - self.num_guesses), self.total_guesses, self.guesses)
