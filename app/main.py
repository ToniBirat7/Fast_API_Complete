from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    email: str
    full_name: str = None

class UserOnly(BaseModel):
    id: int
    username: str
    email: str

app = FastAPI()

@app.get("/pq/{usr_id}")
async def path_query(usr_id: int,query: str | None) -> dict[str, str | int]:
  print(f"Query, {query}")
  print(f"Usr Id, {usr_id}")
  return {"msg" : f"Query {query}, Id {usr_id}"}

@app.post("/user/")
async def save_user(user : User) -> dict[str, User]:
  return {"data" : user}

@app.get("/users/{user_id}", response_model=UserOnly)
async def get_user(user_id: int):
    user = User(
        id=user_id,
        username="johndoe",
        email="johndoe@example.com",
        full_name="John Doe"
    )
    return user