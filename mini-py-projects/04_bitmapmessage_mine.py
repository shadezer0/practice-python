"""
Link: https://inventwithpython.com/bigbookpython/project3.html#
"""
print("Enter the message to display with the bitmap.")
message = input("> ")

with open("mini-py-projects/bitmapworld.txt") as f:
    for line in list(f):
        for i, bit in enumerate(line):
            out = message[i % len(message)] if bit != " " else " "
            print(out, end="")
        print()
