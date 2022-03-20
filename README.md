This project implements a simple wordl solver. See tester.py for a simple script that solves every single word.

In general, there are two main functions:
1. best_guess(rules) will take in a dictionary object representing the information about the word we know so far and recommend a next guess.
2. score_word(secret_word, guess_word) will take in the hidden word and a guess to generate a dictionary object representing the knowledge the user would get back.

The algorithm currently assumes letters will not repeat, as the game was originally written.

The tester.py file is intended to simulate the algorithm playing every possible word and recoding the guesses it would make. The analyzer.py file is intended to aggregate results produced by the tester.py file.