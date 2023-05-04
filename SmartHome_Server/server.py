from fastapi import FastAPI
import connection
from bson import ObjectId
from typing import Optional
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import requests
from fastapi_utils.tasks import repeat_every
from training import Classification
import pickle
import random

#Import Models

from datetime import datetime
from datetime import date
import time

app = FastAPI()

origins = ["*"]

data = {"isAutomate": False, "roomTemprature": 72}

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
    roomTemprature: str
    roomHumidity: str

def getTimeDetails():

    today = date.today()

    today = str(today)
    year, month, day = today.split("-")

    year = int(year)
    month = int(month)
    day = int(day)

    season = 1

    if month >= 4 and month <=6:
        season = 2
    elif month >=7 and month <=9:
        season = 3
    elif season >=10 and month <=12:
        season = 4
    time = datetime.now().hour

    return time, day, month, year, season

# API for training mode
@app.post("/personaldata/")
async def create_item(personalData: personalData):
    print("Item ",personalData)

    weatherDetails = getCurrentWeather("Fairfax")

    time, day, month, year, season = getTimeDetails()

    personalDataDict = {}
    personalDataDict["email"] = "vishal@gmu.edu"
    personalDataDict["time"] = time
    personalDataDict["day"] = day
    personalDataDict["month"] = month
    personalDataDict["year"] = year
    personalDataDict["season"] = season
    personalDataDict["roomTemprature"] = personalData.roomTemprature
    personalDataDict["outsideHumidity"] =  weatherDetails["current"]["humidity"]
    personalDataDict["outsidePressure"] =  weatherDetails["current"]["pressure_in"]
    personalDataDict["outsidePrecip"] =  weatherDetails["current"]["precip_mm"]
    personalDataDict["outsideTemprature"] = weatherDetails["current"]["temp_f"]

    data["roomTemprature"] = personalDataDict["roomTemprature"]


    connection.db.personaldata.insert_one(personalDataDict)
    return {"message":"Data recorded for","email": "vishal@gmu.edu", "time": time}

def getCurrentWeather(location):
    print("get weather func...")
    url = "https://weatherapi-com.p.rapidapi.com/current.json"

    querystring = {"q":location}

    headers = {
	"content-type": "application/octet-stream",
	"X-RapidAPI-Key": "ff95de7d70msh2a84c89cc0f71ffp132c5djsn1c6b82a457c0",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    # print(response.json())
    return response.json()


@app.get("/getweather")
def getWeather():
    weatherDetails = getCurrentWeather("Fairfax")
    weatherDetails["roomTemprature"] = data["roomTemprature"]
    return weatherDetails

# API for automated mode

@app.get("/automate/")
def Automate():
    
    if data["isAutomate"]:
        print("Changing to Training mode")
        data["isAutomate"] = False
    else:
        print("Changing to Automatic mode")
        data["isAutomate"] = True
    return {"AutomationStatus": data["isAutomate"]}

@app.on_event("startup")
@repeat_every(seconds=10)  # 10 secs
@app.get("/getacstatus/")
def ACControl() -> None:
    if data["isAutomate"]:
        weatherDetails = getCurrentWeather("Fairfax")
        print("Automatic control of AC...")
        filename = 'finalized_model.sav'
        Data = []
        Data.append(weatherDetails["current"]["humidity"])
        Data.append(weatherDetails["current"]["pressure_in"])
        Data.append(weatherDetails["current"]["precip_mm"])
        Data.append(weatherDetails["current"]["temp_f"])

        # loaded_model = pickle.load(open(filename, 'rb'))

        # result = loaded_model.predict(Data)
        # result = loaded_model.score(X_test, Y_test)
        # print(result)
        FanSpeed = random.randint(0,255)
        return FanSpeed
        return {"Automated": 1, "FanSpeed": FanSpeed}
        
    else:
        print("Training mode...")
        return 0
        return {"Automated": 0, "FanSpeed": 100}

@app.get("/trainmodel")
async def TrainModel():
    print("api classification...")
    accuracy = Classification()
    return {"accuracy":accuracy}

@app.get("/automatestatus")
async def TrainModel():
    return {"status":data["isAutomate"]}