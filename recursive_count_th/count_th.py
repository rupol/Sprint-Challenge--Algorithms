'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    # base case
    # word is less than two characters (th is impossible)
    if len(word) < 2:
        return 0

    # recursive case - move left to right through the word
    # if first two letters is "th", recurse while adding 1 to the count
    elif word[0:2] == "th":
        return 1 + count_th(word[1:])
    # else simply recurse
    else:
        return count_th(word[1:])


print(count_th("thoughth"))
