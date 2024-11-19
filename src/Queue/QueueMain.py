from Queue import Queue

q = Queue()
q.enqueue(4)
q.enqueue("dog")
q.enqueue(True)
print(q.size)

print(q.dequeue())
print(q.size)
q.enqueue(q.dequeue())
print(q.size)
print(q.dequeue())
