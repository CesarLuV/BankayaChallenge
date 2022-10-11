'''Logic for processing KANTO pokemon information.'''
from typing import Dict
from common import utils as u
from common.api_consumer import consume_api
from models.models import Location
from common.constants import KANTO


class KantoServices:
    def __init__(self, locations_in: Location) -> None:
        
        locations_api = self.__consume_api_kanto_locations()
        
        if locations_api.get('error'):
            raise Exception(locations_api.get('error'))
        
        locations_api = u.get_names_all_locations(locations_api.get("locations"))

        locations_normalized = u.get_list_unique_elements(
            u.normalize_list_string_elements(locations_in.locations))
        
        valid_invalid_locs = u.get_valid_invalid_locations(
            locations_normalized, locations_api)
        self.__valid_locations = valid_invalid_locs['valid_locations']
        self.__invalid_locations = valid_invalid_locs['invalid_locations']


    def __consume_api_kanto_locations(self) -> Dict:
        result = consume_api(path=KANTO)
        if result.get("error"):
            return {"result": result}
        return {"locations": result["locations"]}


    def __str__(self) -> str:
        return f'Valid locations: {self.__valid_locations}\n \
            Invalid locations: {self.__invalid_locations}'


    def get_response(self):
        res = dict()
        res['valid_locations'] = self.__valid_locations
        res['invalid_locations'] = self.__invalid_locations
        return res
