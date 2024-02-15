from fastapi import FastAPI

app = FastAPI()


@app.get("/hit")
def greet():
  return "Hello? World?"
