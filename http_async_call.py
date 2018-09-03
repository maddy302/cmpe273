#When your porgram is making a request, it waits for the response.
#In some cases it is acceptable and in some it is not.
#Threading - when 5 process take care of each process individually
#Asynchronous - when a single process defers/ context switch to another process in case of waiting
#For ex - Typical tasks involved in a software engineer's it to develop, build, test, deploy, manage, document
#A multi threading is a concept where two or more employees handle the tasks assigned to them
#Asyncronous means - a engineer is developing, when certain modules are completed, he parks
#his task of development and starts testing, deployment, in the meanwhile he may start documentation.
#i.e He doesn't wait for the response of the deployment team and continues with the others tasks.
#One way to do asynchronous programming is with an event loop. The event loop is exactly what it sounds like, there is a queue of events/jobs and a loop that just constantly pulls jobs off the queue and runs them. These jobs are called coroutines.

#Comparison - To prevent blocking we can use threads or async. 
#Threads have resource starvation, resource allocation, race condition + context switching overhead issues.
#Callback - after the event a process is run, it will attend it when there is a callback response.

#asyncio --
#CPU Context switching - CPU contxt switching is eliminated in this case , as it has application controlled context switching
#Race conditions - because asyncio only runs a single routine at a time
#Deadlock - No race conditions, no deadlocks
#starvation - No new thread is craeted and hence no new resources required

#async keyworkd before the def 
#import requests
import asyncio
import aiohttp
url = "https://webhook.site/41fe4a73-b596-4bf8-a616-e459544d5f62"
urls = [url]*5

def get_url(res):
    print(res.headers['Date'])
    f = open("output.txt","a")
    f.write("Async call "+res.headers['Date']+"\n")
    f.close()

async def get_url_aync(url):
    async with aiohttp.ClientSession() as session:
            async with session.get(url) as res:
                print(res.headers['Date'])
                # print(res.headers['Date'])
                f = open("output.txt","a")
                f.write("Async call "+res.headers['Date']+"\n")
                f.close()

runs = [get_url_aync(url) for url in urls]
single = asyncio.get_event_loop()
single.run_until_complete(asyncio.wait(runs))