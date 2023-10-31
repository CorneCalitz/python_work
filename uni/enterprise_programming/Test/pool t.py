import threading


def increment(threadName):
    x = 0
    for i in range(1_000_000):
        x += i
    print(f"The thread with name = {threadName} produced a sum of: {x}")


t1 = threading.Thread(target=increment, args=("t1",))
t1.start()
t1.join()
