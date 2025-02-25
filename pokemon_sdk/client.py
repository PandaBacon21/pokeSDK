import requests
from .models.models import Pokemon, Generation, Pagination, PaginationResults

BASE_URL = 'https://pokeapi.co/api/v2'

class PokeAPI:
    
    def __init__(self, base_url=BASE_URL): 
        '''initialize the PokeAPI instance with the base_url'''
        
        self.base_url = base_url
    
    def get_pokemon(self, pokemon=None): 
        '''method for retreiving data from /pokemon/{id or name} endpoint'''

        endpoint = '/pokemon'
        if pokemon: 
            results = self._fetch_single_data(endpoint=endpoint, model=Pokemon, target=pokemon)
            if results: 
                print(f'Pokemon retrieved: {results.name}')
        else: 
            results = self._fetch_paginated_data(endpoint=endpoint, model=Pagination)
            if results: 
                print(f'Number of Pokemon retrieved: {results.count}')
        return results

    def get_generation(self, generation=None):
        '''method for retreiving data from /generation/{id or name} endpoint'''

        endpoint = '/generation'
        if generation: 
            results = self._fetch_single_data(endpoint=endpoint, model=Generation, target=generation)
            if results: 
                print(f'Generation Retrieved: {results.name}')
        else: 
            results = self._fetch_paginated_data(endpoint=endpoint, model=Pagination)
            if results: 
                print(f'Number of Generations retrieved: {results.count}')
        return results

    def _fetch_single_data(self, endpoint, model, target): 
        '''utility method to actually fetch the data from the API'''

        full_endpoint = f'{endpoint}/{target}'
        full_url = self.base_url+full_endpoint

        try: 
            res = requests.get(url=full_url)
            res.raise_for_status()
            data = res.json()
            validated_data = model(**data)
            return validated_data       
        except requests.RequestException as e: 
            print(f'Error retrieving {full_endpoint}: {e}')

        except ValueError as e: 
            print(f'Data Validation error: {e}')
        return None

    def _fetch_paginated_data(self, endpoint, model):
        '''utility method to actually fetch the data from the API when pagination is required'''

        full_url = self.base_url+endpoint

        results = []
        count = 0

        while full_url: 
            try: 
                res = requests.get(url=full_url)
                res.raise_for_status()
                data = res.json()
                validated_data = model(**data)
                results.extend(validated_data.results)
                count = validated_data.count
                full_url = validated_data.next
            except requests.RequestException as e:
                print(f'Error retrieving {endpoint}: {e}')
                return None
            except ValueError as e: 
                print(f'Data Validation error: {e}')
                return None 
        try: 
            validated_results = PaginationResults(**{'results': results, 'count': count})
            return validated_results
        except ValueError as e:
            print('Data Validation error: {e}')
            return None






