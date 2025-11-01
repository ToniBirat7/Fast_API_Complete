from fastapi import FastAPI

app = FastAPI()

@app.get("/home/{user_id}/")
async def home(user_id : int) -> dict[str, str | int]:
  return {"msg" : f"Welcome Home {user_id}"}

@app.get("/home/")
async def home_query(query: str) -> dict[str, str | int]:
  print(f"Query, {query}")
  return {"msg" : f"Query {query}"}