from pydantic import BaseModel

class Item(BaseModel):
    item_name: str = "Empty"
    quantity: int = 0


class ItemDB(Item):
    row_no: int
    column_no: int


class Rack(BaseModel):
    is_empty: bool = True
    item_name: str = "Empty"
    quantity: int = 0