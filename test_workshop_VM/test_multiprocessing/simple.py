from multiprocessing import Process, Value, Array
import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print('hello', name)


def f2(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]

if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()

    num = Value('d', 0.0)
    arr = Array('i', range(10))

    p = Process(target=f2, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])

