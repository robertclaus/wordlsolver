from collections import defaultdict
import json

with open('scores.json') as f:
    scores = json.loads(f.read())

total_count = 0
total_guesses = 0
guess_distribution = defaultdict(lambda: 0)
for key, value in scores.items():
    total_count += 1
    total_guesses += value["count"]
    guess_distribution[value["count"]] += 1
    if value["count"] == 8:
        print(f"{key} is particularly hard.")
        print(f"   Guesses were: {value['guesses']}")

print(f"Average Guesses: {total_guesses / total_count}")

print(f"Guess Distribution: {guess_distribution}")