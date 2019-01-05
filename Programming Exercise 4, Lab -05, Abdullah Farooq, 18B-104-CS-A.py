print('Programming Exercise 4')

def palindrome(word):
    word = word.casefold()
    rev_word = reversed(word)
    if list(word) == list(rev_word):
        print('Yes, your string is a palindrome.')
    else:
        print('Sorry, your string is not a palindrome.')
