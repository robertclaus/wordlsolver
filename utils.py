

from collections import defaultdict


mem_words = None
mem_words_by_letter = None
all_letters = [chr(i) for i in range(97, 123)]

def get_words():
    global mem_words, mem_words_by_letter
    if mem_words:
        return mem_words.copy(), mem_words_by_letter.copy()

    with open('words.txt') as f:
        words = f.read().splitlines()

    # Filter words with repeated letters
    duplicate_letter_words = []

    for word in words:
        for letter in word:
            if word.count(letter) != 1:
                duplicate_letter_words.append(word)
                break

    words = list(filter(lambda word: word not in duplicate_letter_words, words))
    mem_words = words
    
    words_by_letter_contains = defaultdict(lambda: [])
    for word in words:
        for letter in word:
            words_by_letter_contains[letter].append(word)
    mem_words_by_letter = words_by_letter_contains

    return words,words_by_letter_contains

def apply_rules(letter_rules):
    # Eliminate words that break known rules
    words_by_letter = mem_words_by_letter
    words = set(mem_words)
    
    for rule in letter_rules:
        if rule["rule"] == "out":
            for word in words_by_letter[rule["letter"]]:
                words.discard(word)
        elif rule["rule"] == "confirmed":
            for word in list(words):
                if word[rule["position"]-1] != rule["letter"]:
                    words.discard(word)
        elif rule["rule"] == "exists":
            for word in list(words):
                if rule["letter"] not in word:
                    words.discard(word)
        elif rule["rule"] == "notposition":
            for word in list(words):
                if word[rule["position"]-1] == rule["letter"]:
                    words.discard(word)
    return list(words)

def confirmed_letters(letter_rules):
    letters_to_ignore = set()
    for rule in letter_rules:
        if rule["rule"] == "confirmed":
            letters_to_ignore.add(rule["letter"])
    return letters_to_ignore

def word_scores(possible_words, letters_to_ignore):
    words = mem_words

    letter_frequency = defaultdict(lambda: 0)
    word_score = defaultdict(lambda: 0)

    # Get letter frequency (number of words with those letters)
    for word in possible_words:
        for letter in word:
            if letter not in letters_to_ignore:
                letter_frequency[letter] += 1
            
    # Get number of words that would be eliminated by picking this word
    for word in words:
        for letter in word:
            word_score[word] += letter_frequency[letter]

    return word_score

def get_best_word(word_score, possible_words):
    if len(possible_words) == 1:
        return possible_words[0], 1
    
    best_word, max_score = "", 0
    for word, score in word_score.items():
        if score >= max_score:
            best_word = word
            max_score = score
    
    return best_word, max_score

def log(word_score, possible_words):
    guess_order = sorted(word_score.items(), key=lambda keyval: keyval[1], reverse=True)

    print("Good words to elminate:")
    print(guess_order[0:5])

    print(f"Some words that could match ({len(possible_words)} words left):")
    for w in possible_words[0:5]:
        print(f"{w} - {word_score[w]}")