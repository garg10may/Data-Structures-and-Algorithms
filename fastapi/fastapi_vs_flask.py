#writing just some sample code to test the performance of fastapi

from fastapi import FastAPI
import uvicorn
import gunicorn
import time
import threading
from threading import current_thread, Thread
from flask import Flask
import gunicorn
import asyncio
from contextlib import asynccontextmanager
from typing import Iterator
import anyio


app = FastAPI()

counter = 0


'''
#very bad code, having a CPU bound code in async function
@app.get("/")
async def read_root():
    print("root route")

    global counter
    counter += 1
    print(counter)
    time.sleep(3)
    return {"message": "root route"}


# Ok, we removed the async keyword, now we have a CPU bound code in sync function, better but 
# this is not what fastapi is meant for, these are run in external threadpool where only 40 threads are allowed
# so if we have 40 requests in parallel, then only 40 requests will be processed at a time, rest will be queued
# and this is not what we want, we want to process 1000 requests in parallel
@app.get("/")
def read_root():
    print("root route")

    global counter
    counter += 1
    print(counter)
    time.sleep(3)
    return {"message": "root route"}


# Let's remove 40 thread limit, and let's see how fastapi works, but this is growing too technical,
# you would be able to process about 250 requests in parallel even when I have set 1000 tokens this is because of the 
# limitation of python with all threads spawning and all the overheads it's able to handle 250 requests in parallel
@asynccontextmanager
async def lifespan(app: FastAPI) -> Iterator[None]:
    limiter = anyio.to_thread.current_default_thread_limiter()
    limiter.total_tokens = 1000
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    print("root route")

    global counter
    counter += 1
    print(counter)
    time.sleep(3)
    return {"message": "root route"}

'''

class Config:
    use_uvloop = False
    loop = "asyncio"


#good code, but need to be async totally, any CPU bound code will be very bad
@app.get("/")
async def read_route():
    print("start")
    global counter
    counter += 1
    print(counter)
    await asyncio.sleep(1)
    print("end")
    return {"message": "read route"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8003)



#fastapi is taking 40 request in parallel with 1 worker or 10 workers)


#sample flask app to test the performance


# app = Flask(__name__)

# counter = 0

# @app.route("/")
# def read_root():
#     global counter
#     counter += 1
#     print(counter)
#     time.sleep(1)
#     return {"message": "Hello, World!"}


# @app.route("/count")
# def count_threads():
#     return {
#         "active_threads": threading.active_count(),
#         "current_thread": current_thread().name,
#         "all_threads": [thread.name for thread in threading.enumerate()]
#     }

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8003)

