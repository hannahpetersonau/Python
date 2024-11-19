from timeit import Timer


# Function that uses concatenation to build a list
def concat_test():
    l = []
    for i in range(1000):
        l = l + [i]


# Function that uses the append method to build a list
def append_test():
    l = []
    for i in range(1000):
        l.append(i)


# Function that uses list comprehension to build a list
def comp_test():
    l = [i for i in range(1000)]


# Function that uses the list() constructor with range to build a list
def range_test():
    l = list(range(1000))


# Timer for concatenation test
t1 = Timer("concat_test()", "from __main__ import concat_test")
print(f"concatenation: {t1.timeit(number=1000):15.2f} milliseconds")

# Timer for append test
t2 = Timer("append_test()", "from __main__ import append_test")
print(f"appending: {t2.timeit(number=1000):19.2f} milliseconds")

# Timer for list comprehension test
t3 = Timer("comp_test()", "from __main__ import comp_test")
print(f"list comprehension: {t3.timeit(number=1000):10.2f} milliseconds")

# Timer for list range test
t4 = Timer("range_test()", "from __main__ import range_test")
print(f"list range: {t4.timeit(number=1000):18.2f} milliseconds")
