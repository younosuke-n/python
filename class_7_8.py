import threading, time

class SumThread(threading.Thread):
    def __init__(self, count):
        threading.Thread.__init__(self)
        self.count = count
        self.return_value = None   # RETURN VALUE

    def run(self):
        sum_value = 0
        for i in range(1, 1 + self.count):
            sum_value += i
            time.sleep(0.1)
        self.return_value = sum_value   # SET RETURN VALUE

    def get_value(self):  # GETTER METHOD
        return self.return_value

class OddThread(SumThread):
    def run(self):
        sum_value = 0
        for i in range(1, 1 + self.count):
            if i % 2 == 1:
                sum_value += i
                time.sleep(0.1)
        self.return_value = sum_value

thread1 = SumThread(5)
thread2 = OddThread(5)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print(thread1.get_value())   # 15
print(thread2.get_value())