'''uvicorn main:app --reload'''

from fastapi import APIRouter
from typing import Optional
from pydantic import BaseModel


router = APIRouter(
    prefix="/user",
    tags=["User"],
    responses={404: {"message": "Not found"}}
)


class Item(BaseModel):
    id: int
    name: str
    item_type: Optional[str] = "a"
    total: int

@router.get("/{user_id}")
async def get_user_by_id(user_id: int, type: Optional[str] = "normal"):
    return {"user_id": user_id, "type": type}

@router.post("/")
def create_item(item: Item):
    return item
