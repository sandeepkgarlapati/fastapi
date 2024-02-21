from fastapi import FastAPI, Header, Body, Response

app = FastAPI()

# @app.get("/happy")
# def happy(status_code=405):
#     return " :)) "

@app.get("/header/{name}/{value}")
def header(name: str, value: str, response:Response):
    response.headers[name] = value
    return "normal body" 


@app.post("/agentt")
def get_agent(user_agent:str = Header()):
    return user_agent