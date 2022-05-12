from flask import Flask, render_template, url_for, request, redirect
from config import settings
from helper import initialise_inventory, insert_new_item, fetch_item
from schemas import Item
import requests

app = Flask(__name__)

@app.route('/')
def index():
    inventory = initialise_inventory()
    return render_template('index.html', inventory=inventory, total_rows=settings.TOTAL_ROWS, total_cols=settings.TOTAL_COLUMNS, BASE_URL=settings.BASE_URL)


@app.route('/insert', methods=['POST', 'GET'])
def insert_new():
    if request.method == 'POST':
        item_name = request.form['item_name']
        quantity = request.form['quantity']
        new_item = Item(
            item_name=item_name,
            quantity=quantity
        )
        insert_response = insert_new_item(new_item)
        insert_response.raise_for_status()
        return redirect('/')
    
    return render_template('insert.html')


@app.route('/fetch', methods=['POST', 'GET'])
def retreive_item():
    if request.method == 'POST':
        item_name = request.form['item_name']
        row_no = int(request.form['row_no'])
        column_no = int(request.form['column_no'])
        quantity = int(request.form['quantity'])
        fetch_response = fetch_item(row_no, column_no, quantity)
        print(fetch_response)
        return redirect('/')
    
    else:
        row_no = request.args.get('row_no')
        column_no = request.args.get('column_no')
        item_name = request.args.get('item_name')
        quantity = request.args.get('quantity')
        return render_template('fetch.html', row_no=row_no, column_no=column_no, item_name=item_name, quantity=quantity)

if __name__ == "__main__":
    app.run(debug=True)