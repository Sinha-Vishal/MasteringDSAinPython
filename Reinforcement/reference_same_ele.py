# R-1.8 
# Python allows negative integers to be used as indices into a sequence,
# such as a string. If string s has length n, and expression s[k] is used for index −n≤k<0,
# whatistheequivalent index j≥0such thats[j] references the same element?

def equivalentIndex(s, k):
    n = len(s)
    equivalIndex = 0
    
    if -n <= k < 0:
        equivalIndex = n + k
        print("k refers to", s[-k], "and j refers to", s[equivalIndex])
        
    return equivalIndex

print(equivalentIndex("hello", -3))
        
    
        
            
    
    