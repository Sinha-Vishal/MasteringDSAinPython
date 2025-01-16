# C-1.19 
# Demonstrate how to use Python’s list comprehension syntax to produce
# the list [ a , b , c , ..., z ], but without having to type all 26 such
# characters literally.

def list_comp_alphabet():
    # return [chr(i) for i in range(97, 97+26)]
        # OR
    return [chr(ord('a') + i) for i in range(26)]


print(list_comp_alphabet())