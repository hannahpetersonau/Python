import timeit
from LinkedStack import LinkedStack

def empty(stack):
    return stack.is_empty

def push(stack, num_elements):
    for i in range(num_elements):
        stack.push(i)

def pop(stack, num_elements):
    for i in range(num_elements):
        stack.pop()

def peek(stack):
    if not stack.is_empty:
        return stack.peek()
    return None

def sizing(stack):
    return stack.sizing

def main():
    input_sizes = range(100, 1001, 20)
    print(f"{'n':<10}{'is_empty':<10}{'push':<10}{'pop':<10}{'peek':<10}{'size':<10}")

    for sizing in input_sizes:
        stack = LinkedStack()
        is_empty_time = timeit.timeit(lambda: empty(stack), number=100) / 100
        push_time = timeit.timeit(lambda: push(stack, 1), number=100) / 100
        pop_time = timeit.timeit(lambda: pop(stack, 1), number=100) / 100
        peek_time = timeit.timeit(lambda: peek(stack), number=100) / 100
        sizing_time = timeit.timeit(lambda: stack.size, number=100) / 100

        print(
            f"{sizing:<10}{is_empty_time:<10.6f}{push_time:<10.6f}{pop_time:<10.6f}{peek_time:<10.6f}{sizing_time:<10.6f}")

if __name__ == "__main__":
    main()