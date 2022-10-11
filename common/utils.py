'''Script for utilities tools.'''

from typing import List, Dict


def get_list_unique_elements(elements_list: List) -> List:
    return list(set(elements_list))


def normalize_list_string_elements(elements_list: List[str], 
                            lower_case: bool = True) -> List[str]:
    normalized_list = list()
    if lower_case:
        for elem in elements_list:
            normalized_list.append(elem.lower().strip())
    else:
            normalized_list.append(elem.upper().strip())
    return normalized_list


def get_names_all_locations(locations: List[object]) -> List[str]:
    location_names = [elem['name'] for elem in locations]
    return location_names


def get_valid_invalid_locations(locations_to_validate: List[str], 
                            location_names: List[str]) -> Dict:
    valid_locations = list()
    invalid_locations = list()
    for location in locations_to_validate:
        if location in location_names:
            valid_locations.append(location)
            continue
        invalid_locations.append(location)
    res = {"valid_locations": valid_locations, "invalid_locations": invalid_locations}
    return res
