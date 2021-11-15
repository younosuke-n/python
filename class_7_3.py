from multiprocessing import Process, Queue
import random

def randin(q):
    while True:
        q.put(int(random.random()*10))

def randout(q):
    while True:
        print(q.get())

if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=randin, args=(q,))
    p1.start()
    p2 = Process(target=randout, args=(q,))
    p2.start()