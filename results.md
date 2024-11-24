For Queue:
    Expected hypothesis: We would expect the execution time to match O(n).
    This is because the presence of enqueue of O(n) should show linear growth, 
    even while dequeue's O(1) operation will be constant, so it should have a 
    linear growth based on the queue.
    Actual: O(n)
    The reason for this is the order of operations was executed correctly, 
    and the averages built linear as the queue grew. These results matched my hypothesis.
    We also took an average of 100 tests to create more accurate results.

![Growth Rate for Queue](/images/Queue.png)


For Stack:
    Expected hypothesis: We would expect the execution time to match O(1).
    This is because the operations should have a constant output as the
    stack increases. The stack contains pushing and popping, which are likely
    to be O(1) because of the order of magnitude of those operations. These
    operations are O(1).
    Actual: O(1)
    The reason for this is the operations are constant (do not rearrange)
    causing the output to be constant. We also took an average of 100 tests to create
    more accurate results.

![Growth Rate for Stack](/images/Stack.png)


For LinkedQueue:
    Expected hypothesis: We would expect the execution time to match O(1).
    This is because the enqueue is adding to the end of a linked list, different to that
    of the Queue.py so this and all other operations are O(1) because they don't move parts 
    of the list.
    Actual: O(1)
    The reason for this is the operations are constant (do not rearrange)
    causing the output to be constant. We also took an average of 100 tests to create
    more accurate results.

![Growth Rate for LinkedQueue](/images/Linked%20Queue.png)


For LinkedStack
    Expected hypothesis: We would expect the execution time to match O(1).
    This is because both pushing and popping are likely to be O(1) because 
    of the order of magnitude of those operations. These operations are O(1).
    Both peek and is_empty don't change the stack so they should also be constant.
    Actual: O(1)
    The reason for this is the operations are constant (do not rearrange)
    causing the output to be constant. We also took an average of 100 tests to create
    more accurate results. 

![Growth Rate for LinkedStack](/images/Linked%20Stack.png)

