# C-1.15 
# Write a Python function that takes a sequence of numbers and determines
# if all the numbers are different from each other (that is, they are distinct).

def isdistinct(seq):
    return len(seq) == len(set(seq))

# data = [3, 6, 2, 8, 4, 3]
data = [3, 6, 2, 8, 4]
print(isdistinct(data))