import pytest
from pokemon_sdk.models.models import Pokemon, Generation, PaginationResults
from pokemon_sdk.client import PokeAPI


client = PokeAPI()

def test_pokemon_name():
    pokemon = client.get_pokemon('bulbasaur')
    assert isinstance(pokemon, Pokemon)
    assert pokemon.name == 'bulbasaur'

def test_pokemon_id_int():
    pokemon = client.get_pokemon(1)
    assert isinstance(pokemon, Pokemon)
    assert pokemon.name == 'bulbasaur'

def test_pokemon_id_str(): 
    pokemon = client.get_pokemon('1')    
    assert isinstance(pokemon, Pokemon)
    assert pokemon.name == 'bulbasaur'

def test_pokemon_all():
    pokemon_all = client.get_pokemon()
    assert isinstance(pokemon_all, PaginationResults)
    assert isinstance(pokemon_all.count, int)

def test_pokemon_fake(): 
    fake_pokemon = client.get_pokemon('taco')
    assert fake_pokemon is None

def test_generation_name():
    generation = client.get_generation('generation-i')
    assert isinstance(generation, Generation)
    assert generation.name == 'generation-i'

def test_generation_id_int():
    generation = client.get_generation(1)
    assert isinstance(generation, Generation)
    assert generation.name == 'generation-i'

def test_generation_id_str():
    generation = client.get_generation('1')
    assert isinstance(generation, Generation)
    assert generation.name == 'generation-i'

def test_generation_all():
    generation_all = client.get_generation()
    assert isinstance(generation_all, PaginationResults)
    assert isinstance(generation_all.count, int)

def test_generation_fake():
    fake_generation = client.get_generation('taco')
    assert fake_generation is None