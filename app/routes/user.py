from typing import List, Optional
from fastapi import APIRouter, HTTPException
from app.models.user import UserModel
from app.config import db
from bson import ObjectId

router = APIRouter()

@router.post("/user/", response_model=UserModel)
async def create_user(user: UserModel):
    user_ = await db["users"].find_one({"username": user.username})
    if user_:
        raise HTTPException(status_code=404, detail="UserName already exists")
    else:
        user_dict = user.dict()
        result = await db["users"].insert_one(user_dict)
        user_dict["_id"] = str(result.inserted_id)
        return user_dict


@router.get("/users/",response_model=List[UserModel])
async def get_user(username: Optional[str] = None):
    if username:
        user = await db["users"].find_one({"username": username})
        if user:
            user["_id"] = str(user["_id"])
            return [user]
        raise HTTPException(status_code=404, detail="User not found")
    
    else:
        user_cursor = db["users"].find()
        users = []
        async for user in user_cursor:
            user["_id"] = str(user["_id"])
            users.append(user)
        return users



@router.get("/user/{username}",response_model=UserModel)
async def get_user(username: str):
    user = await db["users"].find_one({"username": username})
    if user:
        user["_id"] = str(user["_id"])
        return user
    raise HTTPException(status_code=404, detail="User not found")


@router.put("/user/", response_model=UserModel)
async def update_user(user: UserModel):
    result = await db["users"].update_one({"username": user.username}, {"$set": user.dict()})
    if  result.modified_count == 1:
        return user
    else:
        raise HTTPException(status_code=404, detail="UserName does not exist.")
        
    
@router.delete("/user/{username}")
async def delete_user(username: str):
    result = await db["users"].delete_one({"username": username})
    if result.deleted_count == 1:
        return {"result": f"Successfully deleted {username}."}
    raise HTTPException(status_code=404, detail="User not found")

