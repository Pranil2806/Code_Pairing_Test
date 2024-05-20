from math import factorial

def factorial_str(n):
  if n < 0:
    return "Factorial is not defined for negative numbers"

  # Convert factorial to a string for efficient manipulation
  result = str(factorial(n))

  # Extract and return the first 10 digits
  return result[:10]

# Result for n = 10, 100, 1000
print(factorial_str(10))  # Output: 3628800
print(factorial_str(100)) # Output: 9332621544
print(factorial_str(1000)) # Output: 40238726007
