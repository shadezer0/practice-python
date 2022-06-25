"""
Birthday Paradox Simulation
Link: https://inventwithpython.com/bigbookpython/project2.html#
"""

import datetime, random


def getBirthdays(numberOfBirthdays):
    """Returns a list of random date objects for birthdays"""
    birthdays = []
    for i in range(numberOfBirthdays):
        # Year is unimportant, all should just have same year
        startOfYear = datetime.date(2001, 1, 1)

        # Get a random day into the year
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays):
    """Returns the date object of a birthday that occurs more than once in the birthday list"""
    if len(birthdays) == len(set(birthdays)):
        return None  # All birthdays are unique

    # Compare each birthday to every other one
    for a, birthdayA in enumerate(birthdays):
        for birthdayB in birthdays[a + 1 :]:
            if birthdayA == birthdayB:
                return birthdayA  # Return matching birthday


# Display the intro
print(
    """Birthday Paradox, by Al Sweigart al@inventwithpython.com

The birthday paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.

(It's not actually a paradox, it's just a surprising result.)
"""
)

# Set up a tuple of month names in order
MONTHS = (
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
)

while True:  # Keep asking until user enters valid amount
    print("How many birthdays shall I generate? (Max 100)")
    response = input(">")
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break  # User has entered valid amount
print()

# Generate and display the birthdays:
print(f"Here are {numBDays} birthdays:")
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    monthName = MONTHS[birthday.month - 1]
    dateText = f"{monthName} {birthday.day}"
    print(dateText, end="")
    if i != len(birthdays) - 1:
        print(", ", end="")
print()
print()

# Determine if there are two birthdays that match
match = getMatch(birthdays)

# Display results
print("In this simulation, ", end="")
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = f"{monthName} {match.day}"
    print("multiple people have a birthday on", dateText)
else:
    print("there are no matching birthdays.")
print()

# Run through 100,000 simulations
print(f"Generating {numBDays} random birthdays 100,000 times...")
input("Press Enter to begin...")

print("Let's run another 100,000 simulations.")
simMatch = 0  # How many simulations had matching birthdays in them
for i in range(100000):
    # Report on progress every 10,000 simulations
    if i % 10000 == 0:
        print(i, "simulations run...")
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch += 1
print("100,000 simulations run.")

# Display simulation results
probability = round(simMatch / 100000 * 100, 2)
print(
    f"Out of 100,000 simulations of {numBDays} people there was a matching birthday in that group {simMatch} times. This means that {numBDays} people have a {probability}% chance of having a matching birthday in their group. That's probably more than you would think!"
)
