# C-1.20 
# Python’s random module includes a function shuffle(data) that accepts a
# list of elements and randomly reorders the elements so that each possible 
# order occurs with equal probability. The random module includes a
# more basic function randint(a, b) that returns a uniformly random integer
# from a to b (including both endpoints). Using only the randint function,
# implement your own version of the shuffle function.

import random

def my_shuffle(data):
  for i in range(len(data) - 1, 0, -1):
    j = random.randint(0, i)
    data[i], data[j] = data[j], data[i]

# Example usage:
my_list = [1, 2, 3, 4, 5]
my_shuffle(my_list)
print(my_list)
    