from fastapi import HTTPException, Depends, status
from typing import Annotated,List
import models
from sqlalchemy.orm import Session
from db.config import get_db
from fastapi import APIRouter
from Todo.schemas.serializers import PostResponseSerializer, PostCreateSerializer

api = APIRouter()

db_dependency = Annotated[Session, Depends(get_db)]


'''RESPONSE MODELS (alternative to serializers.py)
# INPUT: What comes IN to your API
from pydantic import BaseModel
class PostBase(BaseModel):
    title: str
    content: str
    user_Id: int

# OUTPUT: What goes OUT from your API (you haven't created this yet)
class PostResponse(BaseModel):
    id: int          # ← Added by database
    title: str
    content: str
    user_Id: int
'''

@api.get("/posts",status_code=status.HTTP_200_OK,response_model=List[PostResponseSerializer])
def read_posts(db:db_dependency):
    posts=db.query(models.Post).all()
    if not posts:
        raise HTTPException(status_code=404, detail='No posts found')
    return posts


@api.get("/posts/{post_Id}", status_code= status.HTTP_200_OK, response_model=PostResponseSerializer)
async def read_post(post_Id: int, db: db_dependency):
    post = db.query(models.Post).filter(models.Post.id == post_Id).first()
    if post is None:
        raise HTTPException(status_code=404, detail='Post was not found')
    return post


@api.post("/posts/", status_code=status.HTTP_201_CREATED,response_model=PostResponseSerializer)
async def create_post(post: PostCreateSerializer, db: db_dependency):
    user_exists=db.query(models.Post).filter(models.User.id== post.user_Id).first()
    if not user_exists:
        raise HTTPException(status_code=400, detail="User does not exist")
    db_post = models.Post(**post.model_dump())
    db.add(db_post)
    db.commit()
    return db_post

@api.delete("/posts/{post_Id}", status_code= status.HTTP_200_OK)
async def delete_post(post_Id: int, db: db_dependency):
    db_post = db.query(models.Post).filter(models.Post.id == post_Id).first()
    if db_post is None:
        raise HTTPException(status_code=404, detail='Post was not found')
    post_id= db_post.id
    db.delete(db_post)
    db.commit()
    return {"message": f"Post with id {post_id} deleted successfully."}


