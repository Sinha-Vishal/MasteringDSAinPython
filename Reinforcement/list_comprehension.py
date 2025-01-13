# R-1.11 
# Demonstrate how to use Python’s list comprehension syntax to produce
# the list [1, 2, 4, 8, 16, 32, 64, 128, 256].

def list_comprehension():
    list_comprehension = [2**i for i in range(9)]
    print(list_comprehension)
    
list_comprehension()    