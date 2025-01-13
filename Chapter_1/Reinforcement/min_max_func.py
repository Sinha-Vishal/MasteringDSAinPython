# R-1.3 
# Write a short Python function, minmax(data), that takes a sequence of
# one or more numbers, and returns the smallest and largest numbers, in the
# form of a tuple of length two. Do not use the built-in functions min or
# max in implementing your solution.

def minmax(data):
    min = data[0]
    max = data[0]
    for i in range(len(data)):
        if data[i] < min:
            min = data[i]
            
        if data[i] > max:
            max = data[i]
            
    return min, max

data = [3, 5, 7, 2, 8, 4]
print(minmax(data))
            

