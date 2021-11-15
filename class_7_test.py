import threading, datetime, time

event = threading.Event()
stop = False  # イベント停止のフラグ

def event_example2():
    print("Thread starts at", datetime.datetime.now())
    count = 0
    while not stop:
        event.wait() # ここで待ち状態になる
        event.clear()
        count += 1
        print(count)
    print("Thread ends at", datetime.datetime.now())

thread = threading.Thread(target=event_example2)
thread.start()

time.sleep(1) # メインスレッドは1秒ここで停止
event.set() # 1秒後にeventで待っているスレッドを起こす
time.sleep(1) # メインスレッドは1秒ここで停止
event.set() # 1秒後にeventで待っているスレッドを起こす
time.sleep(1) # メインスレッドは1秒ここで停止
stop = True
event.set()

thread.join()