guess_number_oop
================

Motivation
----------
This project is practice for me to modularize code, write an object-orientied program, and upload a package to PyPi. 

Required Libraries
------------------
* random
* sys

Files
-----
<pre>
`guess_number_oop`  
|  
-- `setup.py` (package setup information and metadata)  
|  
-- `guess_number_oop`  
    |  
    --`__init__.py`   
    |  
    -- `LICENSE.md`  
    |  
    -- `setup.cfg` (configuration file)  
    |  
    -- `Game.py` (module containing Game class)  
    |  
    -- `guess_number_oop.py` (module containing code that plays a game)  
</pre>

Results
-------
Running this program will prompt the user to play a game where you have 20 chances to guess a random computer-generated integer between 0 and 1000. The game takes place in a terminal window. After each guess, you will be told whether the number the computer picked is higher or lower than the one you guessed. You will also be shown a list of all of the numbers you have guessed so far. 

Once you succeed in guessing the correct number or you have made 20 unsuccesful guesses, the game will end and you will be asked if you would like to play again.
