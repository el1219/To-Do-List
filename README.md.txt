# Flashcards

A command-line flashcard app built in Python. Add your own cards, quiz yourself, and see which cards you miss the most. Your cards and your mistakes are saved to a file, so your progress is still there the next time you open the program.

## Features
- add: create a new card (front and back)
- quiz: go through all cards in random order and see your score at the end
- hardest: show the card you've missed the most
- Answers ignore capitalization and extra spaces
- Automatically saves and loads cards (and miss counts) from `cards.json`
- Starts cleanly even when the data file doesn't exist yet

## How to run
1. Install Python 3
2. In the terminal, go to the project folder
3. Run: `python flashcards.py`

## Example
add/quiz/hardest/quit: add
Enter front: What is a dict?
Enter back: Key-value pairs
add/quiz/hardest/quit: quiz
What is a dict?
Input your answer: a list
The answer is Key-value pairs
0 / 1
add/quiz/hardest/quit: hardest
What is a dict?: 1 miss(es)
add/quiz/hardest/quit: quit


## What I learned
I built this with a `Card` class and a `Deck` class that holds a list of cards. I used JSON to save and load cards along with their miss counts, random.sample to shuffle the quiz without changing the saved order, and `try / except` to handle a missing data file.