from pydantic import BaseModel
from typing import List, Dict, Optional, Any

class Pokemon(BaseModel): 
    id: int
    name: str
    base_experience: int
    height: int
    is_default: bool
    order: int
    weight: int
    abilities: List[Dict[str, Any]]
    forms: List[Dict[str, Any]]
    game_indices: List[Dict[str, Any]]
    held_items: List[Dict[str, Any]]
    location_area_encounters: str
    moves: List[Dict[str, Any]]
    past_types: List[Dict[str, Any]]
    sprites: Dict[str, Any]
    cries: Dict[str, Any]
    species: Dict[str, Any]
    stats: List[Dict[str, Any]]
    types: List[Dict[str, Any]]

class Generation(BaseModel): 
    id: int
    name: str
    abilities: List[Dict[str, Any]]
    names: List[Dict[str, Any]]
    main_region: Dict[str, Any]
    moves: List[Dict[str, Any]]
    pokemon_species: List[Dict[str, Any]]
    types: List[Dict[str, Any]]
    version_groups: List[Dict[str, Any]]


class Pagination(BaseModel):
    count: int
    next: Optional[str]
    previous: Optional[str]
    results: List[Dict[str, Any]]
