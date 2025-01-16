# P-1.29 
# Write a Python program that outputs all possible strings formed by using
# the characters c , a , t , d , o ,and g exactly once.

from itertools import permutations

def generate_strings():
    
    chars = ['c', 'a', 't', 'd', 'o', 'g']
    
    all_permutations = permutations(chars)
    
    # Convert each permutation to a string and print
    for perm in all_permutations:
        print("".join(perm))

generate_strings()
    