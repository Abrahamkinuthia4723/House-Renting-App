from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.type import HouseType 

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

