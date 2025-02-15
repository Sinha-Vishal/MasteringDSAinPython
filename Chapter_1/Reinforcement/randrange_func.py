# R-1.12 
# Python’s random module includes a function choice(data) that returns a
# random element from a non-empty sequence. The random module includes a 
# more basic function randrange, with parameterization similar to
# the built-in range function, that return a random choice from the given
# range. Using only the randrange function, implement your own version
# of the choice function.


import random


def choice_own_version(data):
  if not data:
    raise IndexError("Empty sequence")

  return data[random.randrange(0, len(data))]

data = [3, 5, 7, 5, 2, 9]
print(choice_own_version(data))
    
    