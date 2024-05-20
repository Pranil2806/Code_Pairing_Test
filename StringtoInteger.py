import re

input_string = "$180,240/y"

# Remove all characters except numbers, ".", "+" or "-".
cleaned_string = re.sub(r"[^\d\-+\.]", "", input_string)

# Try converting the cleaned string to a float, handling potential errors.
try:
  number = float(cleaned_string)
except ValueError:
  print(f"Error: Could not convert '{input_string}' to a number.")
  exit(1)


number = int(number)

print(number)
