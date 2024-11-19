from timeit import Timer

# Create a Timer for the pop(0) operation
pop_zero = Timer("x.pop(0)", "from __main__ import x")

# Create a Timer for the pop() operation (default is the last element)
pop_end = Timer("x.pop()", "from __main__ import x")

# Print column headers
print(f"{'n':10s}{'pop(0)':>15s}{'pop()':>15s}")

# Iterate over the range of list sizes
for i in range(1_000_000, 100_000_001, 1_000_000):
    # Create a list with 'i' elements
    x = list(range(i))

    # Measure the time taken for 1000 executions of pop(0)
    pop_zero_t = pop_zero.timeit(number=1000)

    # Create a new list with 'i' elements (resetting the list)
    x = list(range(i))

    # Measure the time taken for 1000 executions of pop() (default is the last element)
    pop_end_t = pop_end.timeit(number=1000)

    # Print the results in a formatted manner
    print(f"{i:<10,}{pop_zero_t:>15.5f}{pop_end_t:>15.5f}")
