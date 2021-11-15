import multiprocessing as mp
import time
from random import choice

def use_resource(sem, i, c, l):
    sem.acquire()
    l.acquire()
    c.value += 1
    l.release()
    print('Student ID', i, 'is using a PC. #used = ', c.value)
    time.sleep(choice(range(3)))
    l.acquire()
    c.value -= 1
    l.release()
    sem.release()

if __name__ == '__main__':
    sem = mp.Semaphore(10)
    lock = mp.Lock()
    counter = mp.Value('i', 0) # 'i'は型コードで、int型を表す
    
    for num in range(30):
        mp.Process(target=use_resource, args=(sem, num, counter, lock)).start()