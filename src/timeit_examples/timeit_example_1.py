import timeit

# Example: Timing the execution of a simple statement
timer = timeit.Timer("result = 3 + 5")
execution_time = timer.timeit()
print(f"Execution Time: {execution_time} seconds")