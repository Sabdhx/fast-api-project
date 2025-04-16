from fastapi import FastAPI
app = FastAPI()
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
class Post(BaseModel):
  email:str
  password:str
  published:bool = True
  name:str = "Abdullah"
  rating:Optional[int] = None

@app.get("/")
async def root():
  return {"message": "Hello bro"}

@app.post("/createPost")
async def createPost(post_data:Post):
  print(post_data.dict())
  return {"this is the data: ":f"email is {post_data.email} and the password is {post_data.password} the name is {post_data.name} the rating is {post_data.rating}"} 
  # return {"message":post_data.dict()}

  