from fastapi import FastAPI

app = FastAPI(redirect_slashes=False)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello")
async def say_hello():
    return {"message": "Hello!"}

