
from game import score_word
from solver import best_guess
from utils import get_words


# 
words = [
    "their",
    "about",
]
words, words_by_letter = get_words()
scores = {}
word_count = 0
word_limit = 100

for secret_word in words:
    word_count += 1
    guesses = []
    rules = []
    for guess_count in range(1, 10):
        guess_word, score = best_guess(rules, logging=False)
        guesses.append(guess_word)
        if guess_word == secret_word:
            scores[secret_word] = { "guesses": guesses, "count": len(guesses) }
            break
        new_rules = score_word(secret_word, guess_word)
        rules += new_rules
    if word_count > word_limit:
        break
    if word_count % (word_limit / 20) == 0:
        print(f"On word {word_count} of {word_limit}")


import json
  
with open('scores', 'w') as convert_file:
     convert_file.write(json.dumps(scores))