# P-1.34 
# A common punishment for school children is to write out a sentence multiple 
# times. Write a Python stand-alone program that will write out the
# following sentence one hundred times: “I will never spam my friends
# again.” Your program should number each of the {sentences and it should
# make eight different random-looking typos.

import random
import string

def introduce_typos(sentence, num_typos):

  typo_sentence = list(sentence)
  typo_indices = random.sample(range(len(sentence)), num_typos)

  for i in typo_indices:
    replacement = random.choice(string.ascii_letters + string.digits + ' ')
    typo_sentence[i] = replacement

  return ''.join(typo_sentence)

sentence = "I will never spam my friends again."
num_sentences = 100
num_typos = 8

for i in range(1, num_sentences + 1):
  typo_sentence = introduce_typos(sentence, num_typos)
  print(f"{i}. {typo_sentence}")      