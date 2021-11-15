from multiprocessing import Process, Pipe
import random

def randin(conn):
    while True:
        conn.send(int(random.random()*10))
        conn.close()

def randout(conn):
    while True:
        print(conn.recv())

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p1 = Process(target=randin, args=(parent_conn,))
    p2 = Process(target=randout, args=(child_conn,))
    p1.start()
    p2.start()