# P-1.36 
# Write a Python program that inputs a list of words, separated by white
# space, and outputs how many times each word appears in the list. You
# need not worry about efficiency at this point, however, as this topic is
# something that will be addressed later in this book.

def word_count():

    words = input("Enter a list of words separated by spaces: ").strip().split()
    
    word_frequency = {}
    
    for word in words:
        word_frequency[word] = word_frequency.get(word, 0) + 1
    
    # Output the word counts
    print("\nWord Frequencies:")
    for word, count in word_frequency.items():
        print(f"{word}: {count}")

word_count()


    