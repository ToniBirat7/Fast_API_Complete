from fastapi import FastAPI

app = FastAPI()

@app.get("/home/{user_id}/")
async def home(user_id : int) -> dict[str, str | int]:
  return {"msg" : f"Welcome Home {user_id}"}

@app.get("/query")
async def home_query(query: str | None) -> dict[str, str | int]:
  print(f"Query, {query}")
  return {"msg" : f"Query {query}"}

@app.get("/pq/{usr_id}")
async def path_query(usr_id: int,query: str | None) -> dict[str, str | int]:
  print(f"Query, {query}")
  print(f"Usr Id, {usr_id}")
  return {"msg" : f"Query {query}, Id {usr_id}"}