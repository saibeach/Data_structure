def fibonacci(n):
  fib = [0, 1]
  if n <= len(fib) - 1:
    return fib[n]
  else:
    while n > len(fib) - 1:
      next_fib = fib[-1] + fib[-2]
      fib.append(next_fib)
  return fib[n]

# test cases
print(fibonacci(3) == 2)
print(fibonacci(7) == 13)
print(fibonacci(0) == 0)