#Making the calls in a async way to webhook
import requests
from threading import Thread, Lock
import time
from queue import Queue

lock_on_print = Lock()
q = Queue(maxsize=0)
url1 = "https://webhook.site/41fe4a73-b596-4bf8-a616-e459544d5f62"
q1 = [url1]*5
#print(q1)
def get_url(url):
    res = requests.get(url)
    with lock_on_print:#the lock prevents accessing the print and files simultaneously by different threds
        print(res.headers['Date'])
        f = open("output.txt","a")
        f.write(res.headers['Date']+"\n")
        f.close()
        #print(time.gmtime(time.time))

# print(q)
def process_q():
    while True:
        get_url(q.get())
        q.task_done() #makes sure the q is processed , i.e empty


max_threads = 3
#max threads are respectively started
for i in range(max_threads):
    thread1 = Thread(target = process_q)
    thread1.daemon = True
    thread1.start()
#after all threads are started , it reads the Queue till everything is empty.
#the queue contains the URLS
for i in range(len(q1)):
    q.put(q1[i])
    #print(q1[i])
q.join()
