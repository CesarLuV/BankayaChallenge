'''Logic for processing KANTO pokemon information.'''

from typing import Dict
from common import utils as u
from common.api_consumer import consume_api
from models.models import Location
from common.constants import BASE_EXTERNAL_API_URL, KANTO


class KantoServices:
    def __init__(self, locations_in: Location) -> None:
        
        locations_api = consume_api(uri=BASE_EXTERNAL_API_URL.format(path=KANTO))
        
        if locations_api.get("error"):
            raise Exception(locations_api.get("error"))

        locations_normalized = u.get_list_unique_elements(
            u.normalize_list_string_elements(locations_in.locations))
        
        valid_invalid_locs = u.get_valid_invalid_locations(
            locations_normalized, locations_api["locations"])
        
        self.__valid_locations = valid_invalid_locs["valid_locations"]
        self.__invalid_locations = valid_invalid_locs["invalid_locations"]
        
        # Bonus point a
        self.__best_location = ''
        
        if self.__valid_locations:
            max_pokemons = 0

            for elem in self.__valid_locations:
                res = consume_api(uri=elem["url"])
                if res.get("error"):
                    continue
                elem["areas"] = res["areas"]
                del elem["url"]
                for item in elem["areas"]:
                    res = consume_api(uri=item["url"])
                    if res.get("error"):
                        continue
                    del item["url"]
                    tmp = res["pokemon_encounters"]
                    poke_names = list()
                    for obj in tmp:
                        poke_names.append(obj["pokemon"]["name"])
                    item["pokes"] = poke_names
                    if len(poke_names) > max_pokemons:
                        max_pokemons = len(poke_names)
                        self.__best_location = item["name"]


    def __str__(self) -> str:
        return f'Valid locations: {self.__valid_locations}\n \
            Invalid locations: {self.__invalid_locations}'


    def get_response(self):
        res = dict()
        res["valid_locations"] = self.__valid_locations
        res["invalid_locations"] = self.__invalid_locations
        res["most_diverse_pokemon"] = self.__best_location
        return res
