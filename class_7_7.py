import threading, time, random, os

event = threading.Event()
stop = False

def rps():
    choices = ['Rock', 'Paper', 'Scissors']
    while not stop:
        event.wait()
        event.clear()
        choice = choices[(int(random.random()*10))%3]
        print('choice : %s' % (choice,))

t1 = threading.Thread(target=rps)
t2 = threading.Thread(target=rps)

t1.start()
t2.start()

print('Rock Paper Scissors')
time.sleep(1)
event.set()

stop = True
time.sleep(1)
event.set()

t1.join()
t2.join()