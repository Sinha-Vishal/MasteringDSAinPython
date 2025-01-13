# R-1.4 
# Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the positive integers smaller than n.

def sumSquares(n):
    sum = 0
    
    if n == 0:
        return 0
    
    for i in range(1, n):
        sum += i*i
        
    return sum

print(sumSquares(5))

# R-1.5 
# Give a single command that computes the sum from Exercise R-1.4, rely
# ing on Python’s comprehension syntax and the built-in sum function.

def sumSquaresComp(n):
    
    sum_squares = sum([(i*i) for i in range(1, n) if n > 0])
    return sum_squares

print(sumSquaresComp(5))
        