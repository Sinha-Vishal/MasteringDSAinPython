# C-1.27 
# In Section 1.8, we provided three different implementations of a generator
# that computes factors of a given integer. The third of those implementa
# tions, from page 41, was the most efficient, but we noted that it did not
# yield the factors in increasing order. Modify the generator so that it reports
# factors in increasing order, while maintaining its general performance ad
# vantages.

# from page 41
# def factors(n):
#     k=1
#     while k*k < n:
#         if n%k==0:
#             yield k
#             yield n//k
#         k+=1
        
#         if k*k==n:
#             yield k
            
def factors(n):
    small_factors = []  # To store factors smaller than sqrt(n)
    large_factors = []  # To store factors larger than sqrt(n)
    
    k = 1
    while k * k <= n:
        if n % k == 0:
            small_factors.append(k)  # Append the smaller factor
            if k != n // k:  # Avoid duplication when k is the square root of n
                large_factors.append(n // k)  # Append the larger factor
        k += 1
    
    # Yield factors in increasing order
    for factor in small_factors:
        yield factor
    for factor in reversed(large_factors):
        yield factor
        
print(list(factors(36)))       
