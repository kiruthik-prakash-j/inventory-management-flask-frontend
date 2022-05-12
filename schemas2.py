class ItemDB:
  def __init__(self,item_name: str, quantity: int, row_no: int, column_no: int):
    # self.id = id
    self.name = item_name
    self.quantity = quantity
    self.row_no = row_no
    self.column_no = column_no
    # self.is_empty = is_empty
  def get_details(self):
    print(f"Item name  {self.name}")
    print(f"Item quantity {self.quantity}")
    print(f"Item.row_no {self.row_no}")
    print(f"Item.column_no {self.column_no}")


class Item:
  def __init__(self,item_name: str, quantity: int):
    # self.id = id
    self.name = item_name
    self.quantity = quantity
  def get_details(self):
    print(f"Item name  {self.name}")
    print(f"Item quantity {self.quantity}")
