import requests
from .models import Pokemon, Generation, Pagination

BASE_URL = 'https://pokeapi.co/api/v2'

class PokeAPI:
    
    def __init__(self, base_url=BASE_URL): 
        self.base_url = base_url
    
    def get_pokemon(self, pokemon=None): 
        endpoint = '/pokemon'
        if pokemon: 
            return self._fetch_single_data(endpoint=endpoint, model=Pokemon, target=pokemon)
        return self._fetch_paginated_data(endpoint=endpoint, model=Pagination)

    def get_generation(self, generation=None):
        endpoint = '/generation'
        if generation: 
            return self._fetch_single_data(endpoint=endpoint, model=Generation, target=generation)
        return self._fetch_paginated_data(endpoint=endpoint, model=Pagination)

    def _fetch_single_data(self, endpoint, model, target): 
        # utility function to actually fetch the data from the API
        full_endpoint = f'{endpoint}/{target}'
        full_url = self.base_url+full_endpoint

        try: 
            res = requests.get(url=full_url)
            res.raise_for_status()
            data = res.json()
            validated_data = model(**data)
            print(validated_data.name)
            return validated_data       
        
        except requests.RequestException as e: 
            print(f'Error retrieving {full_endpoint}: {e}')
        except ValueError as e: 
            print(f'Data Validation error: {e}')

    def _fetch_paginated_data(self, endpoint, model):
        full_url = self.base_url+endpoint

        results = []

        while full_url: 
            try: 
                res = requests.get(url=full_url)
                res.raise_for_status()
                data = res.json()
                validated_data = model(**data)
                results.extend(validated_data.results)
                full_url = validated_data.next
                print(validated_data.next)

            except requests.RequestException as e:
                print(f'Error retrieving {endpoint}: {e}')
                break
            except ValueError as e: 
                print(f'Data Validation error: {e}')
                break
        # print(results)
        return results 






