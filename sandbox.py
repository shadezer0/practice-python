import snoop


@snoop
def pig_it(s):
    """Convert string to pig latin. Move the first letter of each word to the end of it,
    then add "ay" to the end of the word."""
    word_list = s.split()
    for i, word in enumerate(word_list):
        if word.isalpha():
            new_word = word[1:] + word[0] + "ay"
            word_list[i] = new_word
    return " ".join(word_list)


print(pig_it("hello world !"))
