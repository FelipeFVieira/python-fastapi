from sqlalchemy.orm import Session
from app.models.item import Item

def get_items(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Item).offset(skip).limit(limit).all()

def create_item(db: Session, name: str):
    db_item = Item(name=name)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_item(db: Session, item_id: int, new_item: Item):
    current_item = db.query(Item).filter(Item.id == item_id).first()

    if current_item:
        current_item.name = new_item.name

        db.commit()
        db.refresh(current_item)
        return new_item
    
    else:
        return None

def delete_item(db: Session, item_id: int) -> Item:
    item = db.query(Item).filter(Item.id == item_id).first()
    
    if item:
        db.delete(item)
        db.commit()
        return item
    else:
        return None
