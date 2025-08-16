"""
File: q2Debug.py

This file contains the script for Question 2 of Homework 1

Fall 2025
Author: <your name here>
"""
# TODO: Put your name above!

"""This script starts with a list of 20 words (randomly generated English words). It loops through the words, keeping 
two accumulator variables (aWords, and tWords). If it finds a word that has an 'a' in it, it adds it to aWords, and
similarly for words that have 't' in them. Then it prints the final lists"""

# TODO: Find the six bugs in this code (one per line, for simplicity), mark each line with a comment describing the bug
# TODO: Correct each bug so that the script works correctly at the end

wordList = ['arch', 'fearful', 'discover', 'add', 'deserve', 'orange', 'annoying', 'uncovered', 'certain', 'mouth',
            'cap', 'bathe', 'encourage', 'abusive', 'jumpy', 'spiky' 'aberrant', 'faint', 'rely', 'unwieldy']

aWords = []
tWords = []
for word in wordList
    if 'a' in word:
        aWords = aWords + word
    if 't' in tWords:
        tWords = [word]

print("A words:")
print(aWords)
print("T words:")
  print(tWords)
