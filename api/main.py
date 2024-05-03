from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    # This will block the event loop - the server will not be able to handle with milions of requests
    very_intense_computation(1000000)

    return {"Hello": "World"}


def very_intense_computation(times: int):
    while times > 0:
        times -= 1
        print(f"Remaining: {times}")
