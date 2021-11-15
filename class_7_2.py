import multiprocessing as mp

def sumprint(start, end):
    result = (start + end) * (end - start + 1) / 2
    print('{:.0f}' .format(result))

if __name__ == '__main__':
    p1 = mp.Process(target=sumprint, args=(1, 10000000))
    p1.start()
    print(sum(range(1,11)))
    p1.join()