"""
Check if a string can be converted into a palindrome by changing only one character.

Input: "abccaa"
Output: Yes
Reason: We can change the 5th char from "a" to "b" to make the string a palindrome
"""


def is_pal(s: str) -> bool:
    """Checks whether the given string is a palindrome"""
    return True if s == s[::-1] else False


def convert_to_pal(s: str) -> bool:
    """Checks whether the given string can be converted
    into a palindrome by only changing one char
    """
    # Since strings are immutable
    s_list = list(s)
    # counter to hold number of characters changed in string
    times_changed = 0
    for i in range(len(s) // 2):
        # Compare corresponding pairs of chars from left and right
        if s[i] != s[len(s) - 1 - i]:
            # if they're not equal, set them as equal
            s_list[i] = s[len(s) - 1 - i]
            s = "".join(s_list)
            times_changed += 1
        # if more than one char was changed
        if times_changed > 1:
            return False
        if is_pal(s):
            return True
    # execution reaches here if len(s) is 1
    return True


if __name__ == "__main__":
    my_strings = ["abcca", "abbcca", "a", "ab"]
    expected = [True, False, True, True]
    for i, s in enumerate(my_strings):
        result = convert_to_pal(s)
        print(result)
        assert result == expected[i], f"{result} result is incorrect"
