from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.type import HouseType
from models.location import Location
from models.pricerange import PriceRange
from models.house import House

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
    return HouseType.find_all()

@app.get('/locations')
def get_locations():
    return Location.find_all()

@app.get('/price_ranges')
def get_price_ranges():
    return PriceRange.find_all()

@app.get('/houses')
def get_houses():
    return House.find_all()

@app.post('/houses')
def save_house(data: House):
    house = House(
        name=data.name,
        type_id=data.type_id,
        location=data.location,
        price_range=data.price_range,
        image_url=data.image_url,
        description=data.description,
        year_of_birth=data.year_of_birth
    )
    house.save()
    return house
