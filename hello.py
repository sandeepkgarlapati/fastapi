from fastapi import FastAPI, Body, Header

app = FastAPI()


@app.get("/hit")
def greet(who):
  return f"Hello? {who}?"

# @app.post("/post")
# def send(who: str = Body(embed=True)):
#   return f'Hello? {who}?' 

# @app.post("/pot")
# def pot_post(who: str = Header()):
#   return f"Hello? {who}?"

@app.post("/agent")
def get_agent(user_agent: str = Header()):
  return user_agent