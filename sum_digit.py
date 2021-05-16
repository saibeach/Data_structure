def sum_digits(n):
  if n < 0:
    ValueError('Inputs 0 or greater only!')
  elif n < 10:
    return n
  else:
    return sum_digits(n // 10)+n % 10

# test cases
print(sum_digits(12))
print(sum_digits(552))
print(sum_digits(123456789))
    