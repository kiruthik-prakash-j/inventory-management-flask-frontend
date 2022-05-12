# Front End Flask Application for the FASTAPI Server

FastAPI server : [https://github.com/kiruthik-prakash-j/inventory-management-fastapi](https://github.com/kiruthik-prakash-j/inventory-management-fastapi)

## Setup

### Clone the repo:
```
git clone 
```

### Create .env file:
```
API_URL=<api-url>/items
AUTHORIZATION_URL=<api-url>/login
USER_EMAIL=<user-email>
USER_PASSWORD=<user-password>
TOTAL_ROWS=<total-rows>
TOTAL_COLUMNS=<total-columns>
BASE_URL=<flask-url>
```

### Create and Activate the virtual Environment

#### For Windows:
```
# Set up the Virtual Environment:
py -3 -m venv venv

# To use the Virtual Environment:
venv\Scripts\activate.bat
```

#### For Linux and Mac:
```
# To set up the Virtual Environment
python3 -m venv venv

# To use the Virtual Environment
source venv/bin/activate
```


### Install dependencies:
```
pip install -r requirements.txt
```

### Run the Application:
```
python app.py
```
