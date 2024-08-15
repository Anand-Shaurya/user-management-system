from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.routes import user

app = FastAPI()

app.include_router(user.router, prefix="/api")

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

app.mount("/static", StaticFiles(directory="static"), name="static")