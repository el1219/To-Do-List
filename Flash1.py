import json
import random
class Card:
    def __init__(self, front, back):
        self.front = front
        self.back = back
        self.misses = 0

    def check(self, guess):
        if guess.lower().strip() == self.back.lower().strip():
            return True

        else:
            self.misses += 1
            return False

class Deck:
    def __init__(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def hardest(self):
        most_misses = None
        no_of_miss = 0
        for x in self.cards:
            if x.misses > no_of_miss:
                most_misses = x
                no_of_miss = x.misses
        return most_misses

    def save(self, filename):
        data = []
        for x in self.cards:
            data.append({"front": x.front, "back": x.back, "misses": x.misses})

        with open(filename, 'w') as f:
            json.dump(data, f)

    def load(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
        for d in data:
            card = Card(d["front"], d["back"])
            card.misses = d["misses"]
            self.add(card)

d = Deck()
try:
    d.load("cards.json")

except FileNotFoundError:
    pass

while True:
    cmd = input("add/quiz/hardest/quit: ").lower()

    if cmd == "add":
        front = input("Enter front: ").lower()
        back = input("Enter back: ").lower()
        d.add(Card(front, back))

    elif cmd == "quiz":
        score = 0

        cards = random.sample(d.cards, len(d.cards))
        for card in cards:
            print(card.front)
            answer = input("Input your answer: ").lower()
            if card.check(answer):    
                score += 1

            else:
                print(f"The answer is {card.back}")
   
        print(f"{score} / {len(d.cards)}")

    elif cmd == "hardest":
        h = d.hardest()
        if h is None:
            print(None)

        else:
            print(f"{h.front}: {h.misses} miss(es)")

    elif cmd == "quit":
        d.save("cards.json")
        break

    else:
        print("Invalid input")