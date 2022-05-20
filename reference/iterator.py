"""
Write a function that takes an iterable as an argument and prints the values of the sequence
"""


def printValues(myIterable):
    myIterator = iter(myIterable)
    try:
        while True:
            print(next(myIterator), end=" ")
    except StopIteration:
        pass


data = [1, 2, 3]
# data = "mystring"
printValues(data)
