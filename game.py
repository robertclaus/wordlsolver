
def score_word(secret_word, guessed_word):
    rules = []
    for i in range(5):
        secret_letter = secret_word[i]
        guessed_letter = guessed_word[i]

        if secret_letter == guessed_letter:
            rules.append({"rule": "confirmed", "letter": secret_letter, "position": i+1})
        elif guessed_letter in secret_word:
            rules.append({"rule": "exists", "letter": guessed_letter})
            rules.append({"rule": "notposition", "letter": guessed_letter, "position": i+1})
        else:
            rules.append({"rule": "out", "letter": guessed_letter})
    rules.reverse()
    return rules

if __name__ == "__main__":
    assert score_word("charm", "frame") == [{'rule': 'out', 'letter': 'f'}, {'rule': 'exists', 'letter': 'r'}, {'rule': 'notposition', 'letter': 'r', 'position': 2}, {'rule': 'confirmed', 'letter': 'a', 'position': 3}, {'rule': 'exists', 'letter': 'm'}, {'rule': 'notposition', 'letter': 'm', 'position': 4}, {'rule': 'out', 'letter': 'e'}]