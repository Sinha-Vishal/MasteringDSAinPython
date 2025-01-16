# C-1.25 Write a short Python function that takes a string s, representing a sentence,
# and returns a copy of the string with all punctuation removed. 
# For example, if given the string "Let s try, Mike.", this function would return
# "Lets try Mike".

import string

def remove_punctuation(sentence):
    clear_text = ''
    for ch in sentence:
        if ch not in string.punctuation:
            clear_text += ch
    return clear_text

print(remove_punctuation("Let's move the place."))
            