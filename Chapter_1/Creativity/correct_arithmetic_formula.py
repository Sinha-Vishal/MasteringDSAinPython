# C-1.26 
# Write a short program that takes as input three integers, a, b,andc, from
# the console and determines if they can be used in a correct arithmetic
# formula (in the given order), like “a+b = c,” “a = b−c,” or “a∗b = c.”

def check_arithmetic_formulas(a, b, c):
    if a + b == c:
        print(f"{a} + {b} = {c}")
    elif a == b - c:
        print(f"{a} = {b} - {c}")
    elif a * b == c:
        print(f"{a} * {b} = {c}")
    else:
        print("No valid arithmetic formula found.")

# Input three integers
try:
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    c = int(input("Enter the value of c: "))

    check_arithmetic_formulas(a, b, c)
except ValueError:
    print("Invalid input! Please enter integers only.")
