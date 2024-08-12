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

@router.get("/user/{username}",response_model=UserModel)
async def get_user(username: str):
    user = await db["users"].find_one({"username": username})
    if user:
        user["_id"] = str(user["_id"])
        return user
    raise HTTPException(status_code=404, detail="User not found")