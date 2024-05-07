from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="src/view")


@router.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})
