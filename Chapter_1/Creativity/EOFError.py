# C-1.21 
# Write a Python program that repeatedly reads lines from standard input
# until an EOFError is raised, and then outputs those lines in reverse order
# (a user can indicate end of input by typing ctrl-D).

def reverse_lines():
  lines = []
  try:
    while True:
      line = input()
      lines.append(line)
  except EOFError:
    pass

  for line in reversed(lines):
    print(line)

# Call the function to read and reverse lines
reverse_lines()