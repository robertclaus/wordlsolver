
from collections import defaultdict

from utils import apply_rules, confirmed_letters, get_best_word, get_words, word_scores, log

def best_guess(letter_rules, logging=False):
    possible_words = apply_rules(letter_rules)
    letters_to_ignore = confirmed_letters(letter_rules)
    word_score = word_scores(possible_words, letters_to_ignore)

    if logging:
        log(word_score, possible_words)

    return get_best_word(word_score, possible_words)
