import threading

x = 0


def increment(threadName, lock):
    lock.acquire()
    global x
    x = 0
    for i in range(1_000_000):
        x += i  # This code expression is not atomic expression, why:
        # the value of x is retrieved from memory
        # the value of x is updated with i
        # the value of x is saved back to memory
    lock.release()
    print(f"The thread with name = {threadName} produced a sum of: {x}")


# Once a thread acquires a lock, no other thread can have access to that critical section
lock = threading.Lock()
t1 = threading.Thread(target=increment, args=("t1", lock))
t2 = threading.Thread(target=increment, args=("t2", lock))
t3 = threading.Thread(target=increment, args=("t3", lock))
t4 = threading.Thread(target=increment, args=("t4", lock))

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()
