import timeit


# Example: Timing the execution of a function
def my_function():
    result = 0
    for i in range(1000000):
        result += i


timer = timeit.Timer("my_function()", setup="from __main__ import my_function")
execution_time = timer.timeit(1)  # Specify the number of executions (in this case, 1)
print(f"Execution Time: {execution_time} seconds")
