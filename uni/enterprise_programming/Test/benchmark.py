def test():
    """Stupid test function"""
    list = []
    for i in range(100):
        list.append(i)

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test()", setup="from __main__ import test"))

    print(timeit.timeit("test()", globals=locals()))