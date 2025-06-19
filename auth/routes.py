from fastapi import APIRouter

router = APIrouter()

@router.post("/login")
    def login():
        return {"message": " login"}

