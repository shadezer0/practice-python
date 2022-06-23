"""
Birthday Paradox Simulation
Link: https://inventwithpython.com/bigbookpython/project2.html#
"""
import random

MAX_SIMULATIONS = 100_000
# A dictionary where each month is mapped to its number of days
MONTHS = {
    "Jan": 31,
    "Feb": 28,
    "Mar": 31,
    "Apr": 30,
    "May": 31,
    "Jun": 30,
    "Jul": 31,
    "Aug": 31,
    "Sep": 30,
    "Oct": 31,
    "Nov": 30,
    "Dec": 31,
}


def main():
    print("How many birthdays shall I generate (Max 100)")
    birthday_count = int(input("> "))
    print(f"Here are {birthday_count} birthdays:")
    # list with all generated birthdays
    birthdays = []

    # Running one simulation
    for i in range(birthday_count):
        random_birthday = generate_birthday()
        if i != birthday_count - 1:
            print(random_birthday, end=", ")
        # comma should not be present after last element
        else:
            print(random_birthday)
        birthdays.append(random_birthday)
    duplicate = check_duplicates(birthdays)
    if duplicate is not None:
        print("In this simulation, multiple people have a birthday on", duplicate)
    else:
        print("In this simulation, duplicate birthdays don't occur")

    # Running simulations
    print(f"Generating {birthday_count} simulations {MAX_SIMULATIONS:,} times...")
    input("Press Enter to begin...")
    print(f"Let's run another {MAX_SIMULATIONS:,} simulations.")
    duplicate_count = run_simulations(birthday_count)
    percent_matching_birthday = (duplicate_count / MAX_SIMULATIONS) * 100

    # Printing results
    print(
        f"Out of {MAX_SIMULATIONS:,} simulations of {birthday_count} people, there was a matching birthday in that group {duplicate_count} times. This means that {birthday_count} people have a {percent_matching_birthday:.2f}% chance of having a matching birthday in their group."
    )
    print("That's probably more than you would think!")


def generate_birthday():
    """
    Returns a random birthday in the format "MONTH DAY". Eg: Jan 5
    """
    # pick a random month from dictionary
    random_month = random.choice(list(MONTHS))
    # pick a random valid day of that month
    random_day = random.randint(1, MONTHS[random_month])
    # return month
    return random_month + " " + str(random_day)


def check_duplicates(my_list):
    """
    Check if a list has duplicate elements and return it.
    Otherwise return None.
    """
    for l in range(len(my_list) - 1):
        r = l + 1
        while r < len(my_list):
            if my_list[l] == my_list[r]:
                return my_list[l]
            r += 1
    return None


def run_simulations(count_per_sim, max_sim=MAX_SIMULATIONS):
    """
    Takes count of dates to generate as an argument, checks and returns the number of duplicates after running max_sim times.
    """
    dup_count = 0
    for sim_count in range(max_sim):
        simulated_birthdays = []
        for _ in range(count_per_sim):
            simulated_birthdays.append(generate_birthday())
        if check_duplicates(simulated_birthdays) is not None:
            dup_count += 1
        if (sim_count + 1) % 10_000 == 0:
            print(f"{sim_count + 1} simulations run...")
    return dup_count


if __name__ == "__main__":
    main()
