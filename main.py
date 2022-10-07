'''The main file for running the app.'''
from fastapi import FastAPI
from typing import Optional
from requests import request


app = FastAPI()


@app.get("/")
def get_root():
    return {"Hello": "Bankaya!"}


@app.get("/cat-facts/{number_facts}")
def get_random_cat_fact(number_facts: int):
    return {"random_fact": number_facts}

