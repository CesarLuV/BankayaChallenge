'''Module for client tests.'''

from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "Bankaya!"}


def test_pokemon_in_location_happy_path_one_poke():
    response = client.post(
                            "/pokemon-in-location/",
                            json={"locations": ["pallet-town"]}
                            )
    assert response.status_code == 200
    assert response.json().get("result") is not None
    assert response.json().get("result").get("error") is None

    json_response = response.json().get("result")

    assert len(json_response.get("invalid_locations")) == 0
    assert len(json_response.get("valid_locations")) == 1

    valid_locations = json_response.get("valid_locations")[0]

    assert len(valid_locations.get("areas")) == 1

    areas = valid_locations.get("areas")[0]

    assert len(areas.get("pokes")) == 20

    assert json_response.get("most_diverse_pokemon") == areas.get("name")


def test_pokemon_in_location_invalid_location():
    response = client.post(
                            "/pokemon-in-location/",
                            json={"locations": ["telesecundaria de Kanto"]}
                            )
    assert response.status_code == 200
    assert response.json().get("result") is not None
    assert response.json().get("result").get("error") is None

    json_response = response.json().get("result")

    assert len(json_response.get("invalid_locations")) == 1
    assert len(json_response.get("valid_locations")) == 0
    assert json_response.get("most_diverse_pokemon") == ''
