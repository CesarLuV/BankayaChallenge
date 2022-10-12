'''Script for utilities tools.'''

from typing import List
from typing import Dict


def get_list_unique_elements(elements_list: List) -> List:
    return list(set(elements_list))


def normalize_list_string_elements(
                                elements_list: List[str],
                                lower_case: bool = True) -> List[str]:

    normalized_list = list()
    for elem in elements_list:
        if lower_case:
            normalized_list.append(elem.lower().strip())
        else:
            normalized_list.append(elem.upper().strip())
    return normalized_list


def get_valid_invalid_locations(
                            locations_to_validate: List[str],
                            locations_list_dict: Dict) -> Dict:

    valid_locations = list()
    invalid_locations = list()

    for elem in locations_list_dict:
        if elem["name"] in locations_to_validate:
            valid_locations.append(elem)
            locations_to_validate.pop(
                locations_to_validate.index(elem["name"]))
            if len(locations_to_validate) == 0:
                break
    invalid_locations = locations_to_validate
    res = {
        "valid_locations": valid_locations,
        "invalid_locations": invalid_locations
        }
    return res
