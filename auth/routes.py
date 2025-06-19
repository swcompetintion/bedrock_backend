from fastapi import APIRouter
from .schemas import UserCreate


router = APIRouter()

@router.post("/singup")
def singup(user: UserCreate):
    return {"email":"user.emailstr"}
