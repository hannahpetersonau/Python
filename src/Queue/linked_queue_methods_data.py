import timeit
from LinkedQueue import LinkedQueue

def empty(queue):
    return queue.is_empty

def enqueue(queue):
    queue.enqueue(20)

def dequeue(queue):
    queue.dequeue()

def size(queue):
    return queue.size

def peek(queue):
    try:
        return queue.peek()
    except Exception:
        pass

def main():
    input_sizes = range(100, 1001, 20)
    print(f"{'n':<10}{'is_empty':<10}{'enqueue':<10}{'dequeue':<10}{'size':<10}{'peek':<10}")

    for sizing in input_sizes:
        queue = LinkedQueue()
        is_empty_time = timeit.timeit(lambda: empty(queue), number=100) / 100
        enqueue_time = timeit.timeit(lambda: enqueue(queue), number=100) / 100
        dequeue_time = timeit.timeit(lambda: dequeue(queue), number=100) / 100
        sizing_time = timeit.timeit(lambda: peek(queue), number=100) / 100
        peek_time = timeit.timeit(lambda: queue.size, number=100) / 100

        print(
            f"{sizing:<10}{is_empty_time:<10.6f}{enqueue_time:<10.6f}{dequeue_time:<10.6f}{sizing_time:<10.6f}{peek_time:<10.6f}")


if __name__ == "__main__":
    main()
