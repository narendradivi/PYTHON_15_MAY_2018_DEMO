import threading
from threading import Thread


class PrintThread(Thread):
    def run(self):
        for i in range(1, 11):
            print(i)


print("Main thread!")
t1 = PrintThread()
t1.start()
print("Count : ", threading.active_count() )
print("End of Main Thread")
