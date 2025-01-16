# P-1.32 
# Write a Python program that can simulate a simple calculator, using the
# console as the exclusive input and output device. That is, each input to the
# calculator, be it a number, like 12.34 or 1034, or an operator, like + or =,
# can be done on a separate line. After each such input, you should output
# to the Python console what would be displayed on your calculator.

def simple_calculator():

  current_value = 0
  operator = None

  while True:
    try:
      user_input = input()
      if user_input.strip() == "":  # Handle empty input
        continue

      if user_input.isnumeric():
        current_value = float(user_input)
        print(current_value)

      elif user_input in ["+", "-", "*", "/"]:
        operator = user_input
        print(operator)

      elif user_input == "=":
        if operator is None:
          print("Error: No operator entered.")
        else:
          try:
            if operator == "+":
              result = current_value + float(input("Enter second operand: "))
            elif operator == "-":
              result = current_value - float(input("Enter second operand: "))
            elif operator == "*":
              result = current_value * float(input("Enter second operand: "))
            elif operator == "/":
              divisor = float(input("Enter divisor: "))
              if divisor == 0:
                print("Error: Division by zero.")
              else:
                result = current_value / divisor
            print(result)
            current_value = result  # Update current value after calculation
            operator = None 
          except ValueError:
            print("Invalid input.")

    except (ValueError, EOFError):
      print("Exiting calculator.")
      break

if __name__ == "__main__":
  simple_calculator()
            
            
        
        
    