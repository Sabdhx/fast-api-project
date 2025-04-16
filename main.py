from fastapi import FastAPI, Response,HTTPException,status
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

my_post = [
    {"name": "Abdullah", "email": "Abdullah@gmail.com", "id": "1"},
    {"name": "Ali", "email": "ali@gmail.com", "id": "2"}
]

class Post(BaseModel):
    email: str
    password: str
    published: bool = True
    name: str = "Abdullah"
    rating: Optional[int] = None

def findSinglePost(id):
    for i in my_post:
        if i["id"] == str(id):
            return i
    return None  # Return None instead of "post not found" to simplify checking

def selectingSpecificOne(id):
  for i,p in enumerate(my_post):
    if p["id"] == id:
      return i


@app.get("/")
async def root():
    return {"message": my_post}

@app.post("/createPost",status_code=status.HTTP_201_CREATED)
async def createPost(post_data: Post):
    print(post_data.dict())
    post_dict = post_data.dict()
    post_dict["id"] = str(randrange(1, 10000))
    my_post.append(post_dict)
    return {"message": post_dict}

@app.get("/post/{id}")
async def getPost(id: int, response: Response):
    print(id)
    post = findSinglePost(id)

    if not post:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post of id: {id} does not found")  

    return {"message": post} 



@app.delete("/post/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletingPost(id: str): 
    index = selectingSpecificOne(id)
    print(index)

    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} not found")

    my_post.pop(index)
    return  # No return since 204 means "no content"
  
@app.patch("/post/putUpdation/{id}",status_code=status.HTTP_201_CREATED)
async def putUpdation(id:str,post: Post):
    index = selectingSpecificOne(id)
    print(index)

    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} not found")
    # my_post["id"] = id
    post_dict = post.dict()
    post_dict['id'] = id
    my_post[index] = post_dict
   
    return {"message":my_post}                