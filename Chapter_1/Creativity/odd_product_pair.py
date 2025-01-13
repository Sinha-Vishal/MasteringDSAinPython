# C-1.14 
# Write a short Python function that takes a sequence of integer values and
# determines if there is a distinct pair of numbers in the sequence whose
# product is odd.

def has_odd_product_pair(seq):
    length = len(seq)
    for i in range(length):
        for j in range(i+1, length):
            if (seq[i] * seq[j]) % 2 != 0:
                return True
    return False
    
data = [1,9,8,3,4]    
print(has_odd_product_pair(data))    