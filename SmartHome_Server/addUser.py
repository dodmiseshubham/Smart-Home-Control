from fastapi import FastAPI
import connection
from bson import ObjectId
from schematics.models import Model
from typing import Optional
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


class Customer(Model):
    cust_id= ObjectId()
    cust_email = Optional[str]
    cust_name = Optional[str]

# An instance of class User
newuser = Customer()

# funtion to create and assign values to the instanse of class Customer created
def create_user(email, username):
    newuser.cust_id = ObjectId()
    newuser.cust_email  = email
    newuser.cust_name = username
    return dict(newuser)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Our root endpoint
@app.get("/")
def index():
    return {"message": "Welcome to FastAPI World"}


class Item(BaseModel):
    name: str
    email: str
    password: str
    age: Optional[float] = None
    address: str

@app.post("/signup/")
async def create_item(item: Item):
    print("Item ",item)

    userData = {}
    userData["email"] = item.email
    userData["name"] = item.name
    userData["password"] = item.password
    userData["age"] = item.age
    userData["address"] = item.address

    user_exists = False
    if connection.db.users.find(
        {'email': item.email}
        ).count() > 0:
        user_exists = True
        print("Customer Exists")
        return {"message":"Customer Exists"}
    # If the email doesn't exist, create the user
    else:
        user_exists == False
    connection.db.users.insert_one(userData)
    return {"message":"User Created","email": item.email, "name": item.name}

class personalData(BaseModel):
    email: str
    time: str
    day: str
    month: str
    year: str
    season: str
    temprature: Optional[float] = None
    humidity: Optional[float] = None
    pressure: Optional[float] = None
    

@app.post("/personaldata/")
async def create_item(personalData: personalData):
    print("Item ",personalData)

    personalDataDict = {}
    personalDataDict["email"] = personalData.email
    personalDataDict["time"] = personalData.time
    personalDataDict["day"] = personalData.day
    personalDataDict["month"] = personalData.month
    personalDataDict["year"] = personalData.year
    personalDataDict["season"] = personalData.season
    personalDataDict["temprature"] = personalData.temprature
    personalDataDict["humidity"] = personalData.humidity
    personalDataDict["pressure"] = personalData.pressure


    connection.db.personaldata.insert_one(personalDataDict)
    return {"message":"User Created","email": personalData.email, "name": personalData.time}

