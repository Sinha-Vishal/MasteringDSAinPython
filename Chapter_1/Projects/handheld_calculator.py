# P-1.33 
# Write a Python program that simulates a handheld calculator. Your program 
# should process input from the Python console representing buttons
# that are “pushed,” and then output the contents of the screen after each operation 
# is performed. Minimally, your calculator should be able to process
# the basic arithmetic operations and a reset/clear operation.

def handheld_calculator():
    print("Welcome to the Handheld Calculator!")
    print("Enter numbers and operators (+, -, *, /).")
    print("Type 'C' to clear/reset the calculator, or 'exit' to quit.")
    
    result = 0  # Initialize the result
    current_input = ""  # Stores the current screen content
    operator = None  # Stores the last operator used
    running = True  # Flag to keep the calculator running

    while running:
        user_input = input(">> ").strip()  # Read input
        
        if user_input.lower() == "exit":
            print("Exiting the calculator. Goodbye!")
            running = False
            continue
        
        if user_input.upper() == "C":
            # Clear/reset the calculator
            result = 0
            current_input = ""
            operator = None
            print("Screen: 0")
            continue
        
        if user_input in ["+", "-", "*", "/"]:
            # Handle operator input
            if operator is not None:
                print("Error: Operator already set. Enter a number next.")
            else:
                operator = user_input
                current_input += f" {operator} "
            print(f"Screen: {current_input.strip()}")
            continue
        
        if user_input.replace('.', '', 1).isdigit() or (user_input[1:].replace('.', '', 1).isdigit() and user_input[0] in "+-"):
            # Handle number input
            if operator is None:
                # First number or result continuation
                result = float(user_input) if current_input == "" else result
            else:
                # Perform the operation
                num = float(user_input)
                if operator == "+":
                    result += num
                elif operator == "-":
                    result -= num
                elif operator == "*":
                    result *= num
                elif operator == "/":
                    if num == 0:
                        print("Error: Division by zero is not allowed.")
                        operator = None
                        continue
                    else:
                        result /= num
                
                operator = None  # Reset the operator after calculation
            current_input = str(result)
            print(f"Screen: {current_input}")
            continue
        
        # Invalid input
        print("Error: Invalid input. Enter a number, operator (+, -, *, /), 'C', or 'exit'.")

# Run the calculator
handheld_calculator()
