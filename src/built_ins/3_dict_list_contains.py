from timeit import Timer
import random

NUM_TESTS = 1000

# Print column headers
print(f"{'n':10s}{'list':>10s}{'dict':>10s}")

# Iterate over the range of sizes
for i in range(10_000, 1_000_001, 20_000):
    # Create a Timer for checking membership in a list
    t = Timer(f"random.randrange({i}) in x", "from __main__ import random, x")

    # Create a list with 'i' elements
    x = list(range(i))

    # Measure the time taken for NUM_TESTS membership checks in a list
    lst_time = t.timeit(number=NUM_TESTS)

    # Create a dictionary with 'i' elements
    x = {j: None for j in range(i)}

    # Measure the time taken for NUM_TESTS membership checks in a dictionary
    dict_time = t.timeit(number=NUM_TESTS)

    # Print the results in a formatted manner
    print(f"{i:<10,}{lst_time:>10.3f}{dict_time:>10.3f}")
