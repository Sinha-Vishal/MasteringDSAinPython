# R-1.2 
# Write a short Python function, is even(k), that takes an integer value and
# returns True if k is even, and False otherwise. However, your function
# cannot use the multiplication, modulo, or division operators.

def is_even(k):
    sum = 0
    while k >= sum:
        if k < 2:
            return False
        
        if k == sum:
            return True
        else:
            sum += 2
    return False

print(is_even(7))