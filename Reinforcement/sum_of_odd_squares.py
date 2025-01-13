# R-1.6 
# Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the odd positive integers smaller than n.

def oddSumSquare(n):
    sum_odd_squares = 0
    
    if n <= 0:
        return 0
    
    for i in range(1, n, 2):
            sum_odd_squares += i*i
    return sum_odd_squares

print(oddSumSquare(5))

# R-1.7 
# Give a single command that computes the sum from Exercise R-1.6, relying 
# on Python’s comprehension syntax and the built-in sum function.

def oddSumSquareComp(n):
    sum_odd_squares = sum([i*i for i in range(1, n, 2) if n > 0])
    return sum_odd_squares

print(oddSumSquareComp(5))
