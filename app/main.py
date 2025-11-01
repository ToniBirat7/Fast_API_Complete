from fastapi import FastAPI
from pydantic import BaseModel

class CreateUser(BaseModel):
  name: str
  age: int
  is_active: bool

app = FastAPI()

@app.get("/pq/{usr_id}")
async def path_query(usr_id: int,query: str | None) -> dict[str, str | int]:
  print(f"Query, {query}")
  print(f"Usr Id, {usr_id}")
  return {"msg" : f"Query {query}, Id {usr_id}"}

@app.post("/user/")
async def save_user(user : CreateUser) -> dict[str, CreateUser]:
  return {"data" : user}