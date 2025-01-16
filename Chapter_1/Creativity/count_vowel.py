# C-1.24 
# Write a short Python function that counts the number of vowels in a given character string.

def count_vowel(sentence):
    vowels = "aeiouAEIOU"
    count = 0
    for letter in sentence:
        if letter in vowels:
            count += 1
    return count

print(count_vowel("Creativity"))