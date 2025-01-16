# P-1.35 
# The birthday paradox says that the probability that two people in a room
# will have the same birthday is more than half, provided n, the number of
# people in the room, is more than 23. This property is not really a paradox,
# but many people find it surprising. Design a Python program that can test
# this paradox by a series of experiments on randomly generated birthdays,
# which test this paradox for n = 5,10,15,20,...,100.

import random

def has_duplicate_birthdays(people):

  birthdays = set()
  for birthday in people:
    if birthday in birthdays:
      return True
    birthdays.add(birthday)
  return False

def birthday_paradox_experiment(n, num_experiments):

  duplicates = 0
  for _ in range(num_experiments):
    birthdays = [random.randint(1, 365) for _ in range(n)] 
    if has_duplicate_birthdays(birthdays):
      duplicates += 1
  return duplicates / num_experiments

def main():
  num_experiments = 1000  # Number of experiments for each value of n
  for n in range(5, 101, 5):
    probability = birthday_paradox_experiment(n, num_experiments)
    print(f"For {n} people: Probability of duplicate birthdays = {probability:.3f}")

if __name__ == "__main__":
  main()
    