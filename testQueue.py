from threading import Thread
from queue import Queue
def worker():
    while True:
        item = q.get()
        print(item)
        q.task_done()

q = Queue()
for i in range(3):
     t = Thread(target=worker)
     t.daemon = True
     t.start()

for item in range(5):
    q.put(item)

q.join()  