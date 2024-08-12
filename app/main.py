from fastapi import FastAPI
from app.routes import user

app = FastAPI()

app.include_router(user.router, prefix="/api")

@app.get("/")
async def read_root():
    return {"message": "FastAPI project made by Anand Shaurya"}