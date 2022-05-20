"""
P - 1.29
Write a Python program that outputs all possible strings formed by using
the characters c , a , t , d , o , and g exactly once. 
"""
# Just printing approach
# def recursion(sub_data, string):
#     if len(sub_data) == 1:
#         print("".join(list(map(str, string + sub_data))), end=",")
#         return
#     else:
#         for i in range(len(sub_data)):
#             new_subdata = [
#                 sub_data[x] for x in range(len(sub_data)) if x != i
#             ]  # Make a list with everything but your current item
#             recursion(new_subdata, string + [sub_data[i]])


# def all_combos(data):
#     assert len(data) > 0, "You have provided an empty string/array"
#     recursion(list(data), [])


# print("Approach 1")
# all_combos("catd")

# P-1.30
# import math

# # Approach 1: Using the log function
# def find_log2(number):
#     assert number > 2, "The number should be greater than 2"
#     return int(math.log(number, 2))


# for x in range(3, 100):
#     print(x, find_log2(x), end=", ")


# P-1.31


# def find_count(val: int, diff: int) -> int:
#     if val > diff:
#         return 0
#     return diff // val


# def make_change(charged: int, given: int) -> dict:
#     # difference between amount given and amount charged
#     diff = given - charged
#     # dictionary to hold count of various denominations of currency
#     count = {}
#     # denominations of currency available
#     denom = [2000, 500, 100, 50, 20, 10, 5, 1]
#     for val in denom:
#         count[val] = find_count(val, diff)
#         diff -= val * count[val]
#     return count


# print(make_change(163, 500))

# P-1.32


# def compute_stack(s):
#     if len(s) == 3:
#         s[0] = int(s[0])
#         s[2] = int(s[2])
#         if s[1] == "+":
#             s[0] = s[0] + s[2]
#         s.pop()
#         s.pop()


# def simple_calculator():
#     stack = []
#     while True:
#         inp = input("> ")
#         if not inp.isdigit() and len(inp) > 1:
#             print("Enter correct input")
#             continue
#         if inp == "=":
#             print(stack.pop())
#         else:
#             stack.append(inp)
#             compute_stack(stack)


# simple_calculator()

# P-1.34

import random

TYPO_COUNT = 5
SENTENCE_COUNT = 20


def create_typo(index, sentences):
    random_pos = -1
    pos_isalpha = False
    # loop till random position is an alphabet
    while not pos_isalpha:
        # Get random position index
        random_pos = random.randrange(0, len(sentences[index]))
        # Check if char is alphabet, break out of loop
        if sentences[index][random_pos].isalpha():
            pos_isalpha = True

    typo = ""
    same_char_typo = True
    # Change typo in case it's the same as the char it's replacing
    while same_char_typo:
        typo = chr(random.randint(ord("a"), ord("z")))
        if typo != sentences[index][random_pos]:
            same_char_typo = False

    # Creating list of characters to modify since string is immutable
    sentence_split = list(sentences[index])

    # Replace char at random position with random char
    sentence_split[random_pos] = typo

    # Join back list of chars to one string
    sentences[index] = "".join(sentence_split)


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
        create_typo(index, sentences)
    return sentences


for i, s in enumerate(write_sentences("I will never spam my friends again.")):
    print(i, ": ", s)
