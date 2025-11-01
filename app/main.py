from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home(req):
  print("Hi,", req)
  return {"msg" : "Welcome Home"}