'''The main file for running the app.'''

from fastapi import FastAPI
from models.models import Location
from service.KantoServices import KantoServices as ks


app = FastAPI()


@app.get("/")
def get_root():
    return {"Hello": "Bankaya!"}


@app.post("/pokemon-in-location/")
def get_pokemon_in_location(locations: Location):
    try:
        obj = ks(locations)
    except Exception as e:
        return {"Error": e.args}
    return {"result": obj.get_response()}
