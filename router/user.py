from fastapi import APIRouter
from fastapi import HTTPException, Depends, status
from typing import Annotated,List
import models
from sqlalchemy.orm import Session
from db.config import get_db
from Todo.schemas.serializers import UserResponseSerializer, UserCreateSerializer

api=APIRouter()
db_dependency = Annotated[Session, Depends(get_db)]
 

'''RESPONSE MODELS (alternative to serializers.py)
# INPUT: What comes IN to your API
from pydantic import BaseModel
class UserBase(BaseModel):
    username:str

# OUTPUT: What goes OUT from your API (you haven't created this yet)
class UserResponse(BaseModel):
    id: int          # ← Added by database
    username: str
'''

  
@api.post("/users/", status_code=status.HTTP_201_CREATED,response_model=UserResponseSerializer)
async def create_user(user: UserCreateSerializer, db: db_dependency):
    db_user = models.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    return db_user

@api.get("/users",status_code=status.HTTP_200_OK,response_model=List[UserResponseSerializer])
async def read_users(db:db_dependency):
    users=db.query(models.User).all()
    if not users:
       raise HTTPException(status_code=404, detail='No users found')
    return users

@api.get("/users/{user_Id}", status_code= status.HTTP_201_CREATED, response_model=UserResponseSerializer)
async def read_user(user_Id: int, db: db_dependency):
    user = db.query(models.User).filter(models.User.id == user_Id).first()
    if user is None:
        raise HTTPException(status_code=404, detail='User not found')
    return user

@api.delete("/users/{user_Id}", status_code= status.HTTP_200_OK)
async def delete_post(user_Id: int, db: db_dependency):
    db_user = db.query(models.User).filter(models.User.id == user_Id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail='User was not found')
    user_id = db_user.id
    db.delete(db_user)
    db.commit()
    return {"message": f"User with id {user_id} deleted successfully."}

  
  

    