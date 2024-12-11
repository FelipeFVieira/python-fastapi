from fastapi import FastAPI, APIRouter

app = FastAPI()

items = {"1": "Item 1", "2": "Item 2", "3": "Item 3"}
@app.get("/read")
def read_items():
    return items

@app.post("/add/{item_name}")
def add_item(item_name: str):
    items[str(len(items) + 1)] = item_name
    return {"message": f"Item {item_name} added!"}

@app.put("/update/{item_id}")
def update_item(item_id: str, item: dict):
    items[item_id] = item["name"]
    return {"message": f"Item {item['name']} updated!"}

@app.delete("/delete/{item_id}")
def delete_item(item_id: str):
    del items[item_id]
    return {"message": f"Item {item_id} deleted!"}



