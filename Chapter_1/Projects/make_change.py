# P-1.31 
# Write a Python program that can “make change.” Your program should
# take two numbers as input, one that is a monetary amount charged and the
# other that is a monetary amount given. It should then return the number
# of each kind of bill and coin to give back as change for the difference
# between the amount given and the amount charged. The values assigned
# to the bills and coins can be based on the monetary system of any current
# or former government. Try to design your program so that it returns as
# few bills and coins as possible.

def make_change(amount_charged, amount_given):

  change = amount_given - amount_charged
  if change < 0:
    raise ValueError("Amount given is less than the amount charged.")

  # Define denominations
  denominations = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1] 
  change_dict = {}

  for denomination in denominations:
    num_coins = change // denomination
    change -= num_coins * denomination
    if num_coins > 0:
      change_dict[denomination] = int(num_coins)

  return change_dict

# Example usage:
amount_charged = 123.50
amount_given = 200.00

try:
  change_dict = make_change(amount_charged, amount_given)
  print("Change:")
  for denomination, count in change_dict.items():
    print(f"{count} x {denomination}")
except ValueError as e:
  print(e)