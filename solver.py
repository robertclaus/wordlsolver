
from collections import defaultdict

from utils import apply_rules, confirmed_letters, get_best_word, get_words, word_scores, log

def best_guess(letter_rules, logging=False):
    words, words_by_letter = get_words()

    possible_words = apply_rules(words, words_by_letter, letter_rules)
    letters_to_ignore = confirmed_letters(letter_rules)
    word_score = word_scores(possible_words, words, letters_to_ignore)

    if logging:
        log(word_score, possible_words)

    return get_best_word(word_score, possible_words)
