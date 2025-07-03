from pydantic import BaseModel
from typing import List

# INPUT SERIALIZERS (what users send TO your API)
class UserCreateSerializer(BaseModel):
    username: str

class PostCreateSerializer(BaseModel):
    title: str
    content: str
    user_Id: int

# OUTPUT SERIALIZERS (what your API sends BACK to users)
class UserResponseSerializer(BaseModel):
    id: int
    username: str
    
    class Config:
        from_attributes = True

class PostResponseSerializer(BaseModel):
    id: int
    title: str
    content: str
    user_Id: int
   

