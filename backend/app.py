from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.type import HouseType 
from models.location import Location

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get('/house_types')
def get_house_types():
    house_types = HouseType.find_all()
    return house_types

@app.get('/locations')
def get_locations():
    locations = Location.find_all()
    return locations

