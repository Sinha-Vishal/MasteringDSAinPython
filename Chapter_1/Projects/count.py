# P-1.30 
# Write a Python program that can take a positive integer greater than 2 as
# input and write out the number of times one must repeatedly divide this
# number by 2 before getting a value less than 2.

def count_repeatedly_divide(n):
    
    if n <= 2:
        return 0
    
    count = 0
    while n >= 2:
        n //= 2
        count += 1
    return count

print(count_repeatedly_divide(10))
    