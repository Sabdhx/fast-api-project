from fastapi import FastAPI, Response,HTTPException,status
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
app = FastAPI()
from datetime import datetime
import time
my_post = [
    {"name": "Abdullah", "email": "Abdullah@gmail.com", "id": "1"},
    {"name": "Ali", "email": "ali@gmail.com", "id": "2"}
]

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    
while True:
    try:
        conn = psycopg2.connect( host="localhost", database="postgres", user="postgres", password="123asd$", cursor_factory=RealDictCursor )
        cursor = conn.cursor()
        print("database is connected successfully")
        break
    except Exception as error:
        print("connecting to database failed")
        print("Error: ",error)
        time.sleep(2)
        
def findSinglePost(id):
    for i in my_post:
        if i["id"] == str(id):
            return i
    return None  

def selectingSpecificOne(id):
  for i,p in enumerate(my_post):
    if p["id"] == id:
      return i


@app.get("/")
async def root():
    cursor.execute("""select * from posts""")
    post = cursor.fetchall()
    return {"message": post}

@app.post("/createPost",status_code=status.HTTP_201_CREATED)
async def createPost(post_data: Post):
        cursor.execute("""insert into posts (title,content,published) values(%s,%s,%s) returning *""",(post_data.title,post_data.content, post_data.published))
        post  = cursor.fetchone()
        conn.commit()
        
        if post == None: 
            raise HTTPException(status_code=status.HTTP_304_NOT_MODIFIED, detail=f"there is an error in creating post")
        
        return {"message":"post successfully","data":post}

@app.get("/post/{id}")
async def getPost(id: int):
    cursor.execute("""select * from posts where id= %s """,(str(id)))
    post = cursor.fetchone()
    return {"message": post} 



@app.delete("/post/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletingPost(id: int): 
  cursor.execute("""delete from posts where id = %s""",(str(id)))
  post  = cursor.fetchone()
  conn.commit()

  if post == None:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"there is no id like the this id: {id}")
  return {"message":"post deleted"}
  
  
  
@app.put("/post/putUpdation/{id}",status_code=status.HTTP_201_CREATED)
async def putUpdation(id:int,post: Post):
    cursor.execute("""update posts set title = %s, content = %s, published = %s where id=%s returning *""",(post.title,post.content,post.published, str(id)))
    updated_post = cursor.fetchone()
    conn.commit()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} not found")
   
    return {"message":updated_post}                