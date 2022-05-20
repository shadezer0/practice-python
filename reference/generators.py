"""
Generators vs functions
"""

MYNUM = 100


def factors(n):
    results = []
    for i in range(1, n + 1):
        if n % i == 0:
            results.append(i)
    return results


def factorsGenerator(n):
    for i in range(1, n + 1):
        if n % i == 0:
            yield i


print(f"The factors of {MYNUM} from regular function: ", factors(MYNUM))

print(f"The factors of {MYNUM} from a generator: ", end="")
for j in factorsGenerator(MYNUM):
    print(j, end=" ")
