from fastapi import FastAPI, APIRouter
from app.repositories.item_repository import *
from app.models.item import Item

app = FastAPI()

router = APIRouter()
@router.get("/read")
def read_items():
    return get_items()

@router.post("/add/{item_name}")
def add_item(item_name: str):
    items[str(len(items) + 1)] = item_name
    return {"message": f"Item {item_name} added!"}

@router.put("/update/{item_id}")
def update_item(item_id: str, item: dict):
    items[item_id] = item["name"]
    return {"message": f"Item {item['name']} updated!"}

@router.delete("/delete/{item_id}")
def delete_item(item_id: str):
    del items[item_id]
    return {"message": f"Item {item_id} deleted!"}

app.include_router(router, prefix="/api/v1")

