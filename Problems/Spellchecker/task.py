dictionary = ["aa", "abab", "aac", "ba", "bac", "baba", "cac", "caac"]


def spell_checker():
    word = input()
    if word in dictionary:
        return 'Correct'
    else:
        return 'Incorrect'


print(spell_checker())
