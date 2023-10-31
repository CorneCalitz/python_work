"""
Every application comes with a process and a main thread.

Disadvantage
 - Large overhead and uses many resources.

Benefit
 - No overhead creation since we have threads.
 - Thread execution is handled by thread pool so program does not need to handle it.
 - Cannot be reused, when a thread is selected and done it is destroyed and returned to a thread pool.

Thread safety: Two or more thread accessing a critical code section is not thread safe. Shared code is not thread safe.

Thread synchronization: mechanism which ensures that two or more threads do not have access to critical code section

Race condition: Two or more threads are trying to access shared data at the same time.
"""

# An example of bad practice

import threading

x = 0

def increment(threadName):
    global x
    x = 0
    for i in range(1_000_000):
        x += i  # This code expression is not atomic expression, why:
        # the value of x is retrieved from memory
        # the value of x is updated with i
        # the value of x is saved back to memory

    print(f"The thread with name = {threadName} produced a sum of: {x}")


t1 = threading.Thread(target=increment, args=("t1",))
t2 = threading.Thread(target=increment, args=("t2",))
t3 = threading.Thread(target=increment, args=("t3",))
t4 = threading.Thread(target=increment, args=("t4",))

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()
