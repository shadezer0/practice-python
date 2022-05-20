# R-1.1
from typing import Iterable


def multiple(n: int, m: int) -> bool:
    return True if n % m == 0 else False


# R-1.2
def is_even(k: int) -> bool:
    return True if k % 2 == 0 else False


# R-1.3
def minmax(data: Iterable) -> int:
    largest = smallest = data[0]
    for val in data[1:]:
        if val > largest:
            largest = val
        if val < smallest:
            smallest = val
    return largest, smallest


# R-1.12
from random import randrange


def my_choice(s):
    while True:
        choice = randrange(min(s), max(s) + 1)
        if choice in s:
            return choice


# C-1.20
from random import randint


def custom_shuffle(data):
    array = [None] * len(data)
    used_indices = set()  # since there won't be duplicates
    for i in range(len(array)):
        added = False
        while added == False:
            choice = randint(0, len(data) - 1)
            if choice not in used_indices:
                array[choice] = data[i]
                used_indices.add(choice)
                added = True
    return array


def custom_shuffle_inplace(data):
    l = len(data)
    for i in range(l):
        choice = randint(0, l - 1 - i)
        data[choice], data[l - 1 - i] = data[l - 1 - i], data[choice]


data = [1, 2, 3, 4, 5, 6]
custom_shuffle_inplace(data)
print(data)
