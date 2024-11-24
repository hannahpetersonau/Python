import timeit
from Queue import Queue

def empty(queue):
    return queue.is_empty

def enqueue(queue, num_elements):
    for i in range(num_elements):
        queue.enqueue(i)

def dequeue(queue, num_elements):
    for i in range(num_elements):
        queue.dequeue()

def size(queue):
    return queue.size

def main():
    input_sizes = range(100, 1001, 20)
    print(f"{'n':<10}{'is_empty':<10}{'enqueue':<10}{'dequeue':<10}{'size':<10}")

    for sizing in input_sizes:
        queue = Queue()
        is_empty_time = timeit.timeit(lambda: empty(queue), number=100) / 100
        enqueue_time = timeit.timeit(lambda: enqueue(queue, sizing), number=100) / 100
        dequeue_time = timeit.timeit(lambda: dequeue(queue, sizing), number=100) / 100
        sizing_time = timeit.timeit(lambda: queue.size, number=100) / 100

        print(
            f"{sizing:<10}{is_empty_time:<10.6f}{enqueue_time:<10.6f}{dequeue_time:<10.6f}{sizing_time:<10.6f}")

if __name__ == "__main__":
    main()
