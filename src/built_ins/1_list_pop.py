from timeit import Timer

# Create a Timer for the pop(0) operation
pop_zero = Timer("x.pop(0)", "from __main__ import x")

# Create a Timer for the pop() operation (default is the last element)
pop_end = Timer("x.pop()", "from __main__ import x")

# Create a list with 2,000,000 elements
x = list(range(2000000))

# Measure and print the time taken for 1000 executions of pop(0)
print(f"pop(0): {pop_zero.timeit(number=1000):10.5f} milliseconds")

# Create a new list with 2,000,000 elements (resetting the list)
x = list(range(2000000))

# Measure and print the time taken for 1000 executions of pop() (default is the last element)
print(f"pop(): {pop_end.timeit(number=1000):11.5f} milliseconds")
