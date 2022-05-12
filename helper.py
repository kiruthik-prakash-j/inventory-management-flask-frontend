import requests
import json
from schemas import Rack, Item, ItemDB
from config import settings


def print_details(item):
    print(f"Name      :{item.item_name}")
    print(f"Quantity  :{item.quantity}")
    print(f"Row no    : {item.row_no}")
    print(f"Column no : {item.column_no}")
    print()


def print_items(itemList):
    for item in itemList:
        print_details(item)
    
    

def get_item_data():
    response = requests.get(url=settings.API_URL)
    response.raise_for_status()
    item_data = response.json()
    return item_data


def get_itemList(dataSet):
    itemList = []
    for data in dataSet:
        item_name = data["item_name"]
        quantity = data["quantity"]
        row_no = data["row_no"]
        col_no = data["column_no"]
        owner_id = data["owner_id"]
        # is_empty = data["is_empty"]

        item = ItemDB(item_name=item_name, quantity=quantity, row_no=row_no, column_no=col_no)
        itemList.append(item)
    
    return itemList


def get_inventory(itemList):
    inventory = [[Rack() for i in range(settings.TOTAL_COLUMNS)] for j in range(settings.TOTAL_ROWS)]
    for item in itemList:
        row_ind = item.row_no
        col_ind = item.column_no
        inventory[row_ind][col_ind].is_empty = False
        inventory[row_ind][col_ind].item_name = item.item_name
        inventory[row_ind][col_ind].quantity = item.quantity

    return inventory


def print_rack(rack):
    print(rack.item_name)
    print(rack.quantity)
    print(rack.is_empty)
    print()


def print_inventory(inventory):
    for row_ind in range(settings.TOTAL_ROWS):
        for col_ind in range(settings.TOTAL_COLUMNS):
            print_rack(inventory[row_ind][col_ind])


def initialise_inventory():
    item_data = get_item_data()
    itemList = get_itemList(item_data)
    inventory = get_inventory(itemList)
    return inventory


def get_first_empty():
    inventory = initialise_inventory()
    for row_ind in range(settings.TOTAL_ROWS):
        for col_ind in range(settings.TOTAL_COLUMNS):
            if inventory[row_ind][col_ind].is_empty == True:
                return (row_ind, col_ind)
    
    return None


def get_token():
    auth_data = {
        "username": settings.USER_EMAIL,
        "password": settings.USER_PASSWORD
    }

    header_data = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    auth_response = requests.post(
        url=settings.AUTHORIZATION_URL,
        data=auth_data,
        headers=header_data
    )
    auth_response.raise_for_status()
    print(auth_response)
    token_data = auth_response.json()
    token = token_data["access_token"]
    
    return token


def get_itemOut(item, row_no, col_no):
    itemOut = ItemDB(
        item_name=item.item_name,
        quantity=item.quantity,
        row_no=row_no,
        column_no=col_no
    )
    return itemOut


def insert_new_item(new_item):
    
    # Get Auth Token
    token = get_token()
    post_header = {
        "accept": "application/json",
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    print("Authorization Successful !")

    # Get empty space
    empty_space = get_first_empty()
    if empty_space == None:
        return f"No empty space found"
    else:
        print(F"Found empty space at {empty_space}")

    # Set the row_no and col_no
    row_no, column_no = empty_space
    
    # Get the item data to be inserted
    itemOut = get_itemOut(new_item, row_no, column_no)
    
    # Set the Post data
    item_data = {
        "item_name": itemOut.item_name,
        "quantity": itemOut.quantity,
        "row_no": itemOut.row_no,
        "column_no": itemOut.column_no,
        "is_empty": False
    }
    post_data = json.dumps(item_data)

    # Insert into the db using API
    print("Inserting the data in the DB")
    post_response = requests.post(
        url=settings.API_URL,
        data=post_data,
        headers=post_header
    )

    return post_response


def get_id(row_no, col_no):
    id_url=f"{settings.API_URL}/getid?row_no={row_no}&column_no={col_no}"
    header_data={"accept": "application/json"}
    response = requests.get(url=id_url, headers=header_data)
    response.raise_for_status()
    id = response.json()
    return id
    pass


def delete_item(id):
    delete_url=f"{settings.API_URL}/{id}"
    # Get Auth Token
    token = get_token()
    header_data = {
        "accept": "*/*",
        "Authorization": f"Bearer {token}"
    }
    print("Authorization Successful !")
    
    # Delete from DB
    print("Deleting from DB")
    response = requests.delete(url=delete_url, headers=header_data)
    response.raise_for_status()
    pass


def fetch_item(row_no, col_no, quantity):

    # Initialise inventory
    inventory = initialise_inventory()
    print(inventory[row_no][col_no].is_empty)
    print(inventory[row_no][col_no].quantity)
    if inventory[row_no][col_no].is_empty == True:
        return f"There is no item here!"
    if inventory[row_no][col_no].quantity < quantity:
        return f"Not enough quantity in inventory!"
    
    # Get the item id from the DB
    id = get_id(row_no, col_no)

    # if quantity in inventory = quantity retreived then delete the entry.
    if inventory[row_no][col_no].quantity == quantity:
        # Delete item from DB
        delete_item(id)
        return print(f"Item removed from DB !")

    # change the item's quantity
    inventory_quantity = inventory[row_no][col_no].quantity
    print(quantity)
    new_quantity = int(inventory_quantity) - int(quantity)
    print(f"new quantity: {new_quantity}")
    item_data = {
        "item_name": inventory[row_no][col_no].item_name,
        "quantity": new_quantity,
        "row_no": row_no,
        "column_no": col_no,
        "is_empty": False
    }
    put_data = json.dumps(item_data)
    put_url = f"{settings.API_URL}/{id}"
    
    # Get Auth Token
    token = get_token()
    post_header = {
        "accept": "application/json",
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    print("Authorization Successful !")

    put_response = requests.put(
        url=put_url,
        data=put_data,
        headers=post_header
    )

    # put_response.raise_for_status()

    return put_response
