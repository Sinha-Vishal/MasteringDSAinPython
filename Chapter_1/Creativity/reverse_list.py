# C-1.13 
# Write a pseudo-code description of a function that reverses a list of n
# integers, so that the numbers are listed in the opposite order than they
# were before, and compare this method to an equivalent Python function
# for doing the same thing.

# Pseudo-code:
# 1. Find the length of the list.
# 2. Create a new list to store the reverse order of elements.
# 3. Run a for loop from the last element to the first element.
# 4. Store the elements in the new list

def reverse_list(nums):
    length = len(nums)
    reverse_lst = []
    
    for i in range(length-1, -1, -1):
        reverse_lst.append(nums[i])
        
    return reverse_lst

data = [4, 6, 8, 3, 1, 9]
print(reverse_list(data))
        
        