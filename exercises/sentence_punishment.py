"""
P-1.34
A common punishment for school children is to write out a sentence 
multiple times. Write a Python stand-alone program that will write out the
following sentence one hundred times: “I will never spam my friends
again.” Your program should number each of the sentences and it should
make eight different random-looking typos.
"""

import random

TYPO_COUNT = 8
SENTENCE_COUNT = 100


def create_typo(typo_sentence):
    """
    Replace a randomly selected alphabetic char in a sentence with a randomly created typo
    """
    random_pos = -1
    pos_isalpha = False
    # loop till random position is an alphabet
    while not pos_isalpha:
        # Get random position index
        random_pos = random.randrange(0, len(typo_sentence))
        # Check if char is alphabet, break out of loop
        if typo_sentence[random_pos].isalpha():
            pos_isalpha = True

    typo = ""
    same_char_typo = True
    # Change typo in case it's the same as the char it's replacing
    while same_char_typo:
        typo = chr(random.randint(ord("a"), ord("z")))
        if typo != typo_sentence[random_pos]:
            same_char_typo = False

    # Creating list of characters to modify since string is immutable
    sentence_split = list(typo_sentence)

    # Replace char at random position with random char
    sentence_split[random_pos] = typo

    # Join back list of chars to one string
    typo_sentence = "".join(sentence_split)
    return typo_sentence


# TODO: implement using generator
def write_sentences(s):
    typo_indices = []
    sentences = [s for _ in range(SENTENCE_COUNT)]

    # generate indices for sentences which will contain typos
    i = 0
    while i < TYPO_COUNT:
        r = random.randrange(0, SENTENCE_COUNT)
        if r not in typo_indices:
            typo_indices.append(r)
            i += 1
    typo_indices.sort()
    print(f"typo indices: {typo_indices}")
    # add typos to the sentences with indices in typo_indices
    for index in typo_indices:
        # create typo in sentences[index]
        sentences[index] = create_typo(sentences[index])
    return sentences


for i, s in enumerate(write_sentences("I will never spam my friends again.")):
    print(f"{i}: {s}")
