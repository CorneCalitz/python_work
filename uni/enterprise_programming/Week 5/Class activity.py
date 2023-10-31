"""Write a program using two threads such that one writes even numbers in increasing order and the other odd numbers
in increasing order with respect to a certain threshold.
For instance, given a value 10.


import threading

# global variable x

x = 0

def increment(threadName, lock):  # critical section in your code
    lock.acquire()
    global x

    if threadName == "Thread even":
        x = 0
        for i in range(10):
            x += 2
            print(x, threadName)

    elif threadName == "Thread odd":
        x = -1
        for i in range(10):
            x += 2
            print(x, threadName)
    lock.release()
    print("Iteration {0}: x = {1}".format(threadName, x))


lock = threading.Lock()

# creating threads
t1 = threading.Thread(target=increment, args=("Thread even",lock))
t2 = threading.Thread(target=increment, args=("Thread odd",lock))

# start threads
t1.start()
t2.start()

t1.join()
t2.join()

Better code
"""

import threading


def even(threshold):
    lock = threading.Lock()
    lock.acquire()
    for i in range(2, threshold + 1, 2):
        print(i)
    lock.release()


def odd(threshold):
    lock = threading.Lock()
    lock.acquire()
    for i in range(1, threshold + 1, 2):
        print(i)
    lock.release()


t1 = threading.Thread(target=even, args=(10,))
t2 = threading.Thread(target=odd, args=(10,))

t3 = threading.Thread(target=even, args=(10,))
t4 = threading.Thread(target=odd, args=(10,))

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

