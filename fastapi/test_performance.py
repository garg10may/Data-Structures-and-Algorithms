#writing just some sample code to test the performance of fastapi

from fastapi import FastAPI
import uvicorn
import gunicorn
import time
import threading
from threading import current_thread, Thread
from flask import Flask

# app = FastAPI()

# @app.get("/")
# def read_root():
#     time.sleep(20)
#     return {"message": "Hello, World!"}

# @app.get("/test")
# def test():
#     return {"message": "Hello, World!"}

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8002)




#sample flask app to test the performance


app = Flask(__name__)

@app.route("/")
def read_root():
    time.sleep(20)
    return {"message": "Hello, World!"}

@app.route("/test")
def test():
    time.sleep(5)
    return {"message": "Hello, World!"}


@app.route("/count")
def count_threads():
    return {
        "active_threads": threading.active_count(),
        "current_thread": current_thread().name,
        "all_threads": [thread.name for thread in threading.enumerate()]
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8003)

