from fastapi import FastAPI
import asyncio
import uvicorn

app_async = FastAPI()

@app_async.get("/hii")
async def greet_async():
    await asyncio.sleep(2)
    return "Hello? World?"

if __name__ == "__main__":
    uvicorn.run("hello_async:app_async")

    
