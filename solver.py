
from collections import defaultdict

from utils import apply_rules, confirmed_letters, get_best_word, get_words, word_scores, log

def best_guess(letter_rules, logging=False):
    possible_words = apply_rules(letter_rules)
    letters_to_ignore = confirmed_letters(letter_rules)
    word_score = word_scores(possible_words, letters_to_ignore)

    if logging:
        log(word_score, possible_words)

    return get_best_word(word_score, possible_words)

if __name__ == "__main__":
    words, words_by_letter = get_words()
    rules = [
        {'rule': 'out', 'letter': 'o'}, 
        {'rule': 'exists', 'letter': 'a'}, 
        {'rule': 'exists', 'letter': 'r'}, 
        {'rule': 'exists', 'letter': 's'}, 
        {'rule': 'notposition', 'letter': 'a', 'position': 1}, 
        {'rule': 'notposition', 'letter': 'r', 'position': 2}, 
        {'rule': 'notposition', 'letter': 's', 'position': 4}, 
        {'rule': 'confirmed', 'letter': 'e', 'position': 5}, 
    ]
    assert "scare" in apply_rules(rules)