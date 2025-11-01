from fastapi import FastAPI

app = FastAPI()

@app.get("/home/{user_id}/")
async def home(user_id : int):
  print(f"Hi, {user_id}")
  return {"msg" : f"Welcome Home {user_id}"}