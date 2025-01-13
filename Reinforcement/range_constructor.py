# R-1.9 
# What parameters should be sent to the range constructor, to produce a
# range with values 50, 60, 70, 80?

def rangeConstructor():

    for i in range(50, 90, 10):
        print(i, end= " ")
        
rangeConstructor()        
    
# R-1.10 
# What parameters should be sent to the range constructor, to produce a
# range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?  
print()

def rangeConstructor_2():

    for i in range(8, -10, -2):
        print(i, end= " ")
        
rangeConstructor_2()    