import multiprocessing as mp
import os

def washer(input, output):
    dish = input.get()
    print('Washing', dish, 'dish')
    output.put(dish)
    input.task_done()

def dryer(input):
    while True:
        dish = input.get()
        print('Drying %s %s dish' % (os.getpid(), dish))
        input.task_done()

if __name__ == "__main__":
    wash_queue = mp.JoinableQueue()
    dry_queue = mp.JoinableQueue()
    dishes = ['salad', 'bread', 'entree', 'dessert']

    for dish in dishes:
        wash_queue.put(dish)

    dryer_proc_1 = mp.Process(target=dryer, args=(dry_queue,))
    dryer_proc_1.daemon = True
    # dryer_proc_2 = mp.Process(target=dryer, args=(dry_queue,))
    # dryer_proc_2.daemon = True
    washer_proc_1 = mp.Process(target=washer, args=(wash_queue,dry_queue,))
    # washer_proc_2 = mp.Process(target=washer, args=(wash_queue,dry_queue,))
    washer_proc_1.start()
    # washer_proc_2.start()
    dryer_proc_1.start()
    # dryer_proc_2.start()

    wash_queue.join()
    dryer_proc_1.join()
    print('Finished!!')