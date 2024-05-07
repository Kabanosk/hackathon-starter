from fastapi import APIRouter, Request, HTTPException
from fastapi.templating import Jinja2Templates

from src.model.users import User

router = APIRouter()
templates = Jinja2Templates(directory="view")


@router.get("/")
async def read_root(request: Request, u_id: int = None):
    if u_id is not None:
        user = User.get_by_id(u_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return templates.TemplateResponse("users.html", {"request": request, "user": user})
    return templates.TemplateResponse("index.html", {"request": request, "msg": "User not found"})
