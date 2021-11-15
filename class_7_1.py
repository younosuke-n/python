import multiprocessing as mp
import os

def washer(dishes, output):
    for dish in dishes:
        print('Washing', dish, 'dish')
        output.put(dish)

def dryer(input):
    while True:
        dish = input.get()
        print('Drying %s %s dish' % (os.getpid(), dish))
        input.task_done()

if __name__ == "__main__":
    dish_queue = mp.JoinableQueue()
    dryer_proc_1 = mp.Process(target=dryer, args=(dish_queue,))
    dryer_proc_1.daemon = True
    dryer_proc_2 = mp.Process(target=dryer, args=(dish_queue,))
    dryer_proc_2.daemon = True
    dryer_proc_1.start()
    dryer_proc_2.start()

    dishes = ['salad', 'bread', 'entree', 'dessert']
    washer(dishes, dish_queue)
    dish_queue.join()
    print('Finished!!')