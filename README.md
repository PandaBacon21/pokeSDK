# PokeAPI Sample SDK

This project is a simple, sample python SDK to simplify working with [PokeAPI](https://pokeapi.co/docs/v2#info). Specifically, the following endpoints:

```
GET https://pokeapi.co/api/v2/pokemon/{id or name}/
GET https://pokeapi.co/api/v2/generation/{id or name}/
```

## Installation

It is highly recommended to use a virtual environment. You can use whichever method you desired, but I prefer [venv](https://docs.python.org/3/library/venv.html).

With your virtual environment active

```
pip install git+https://github.com/PandaBacon21/pokeSDK.git
```

## Usage

```
from pokemon_sdk import PokeAPI
```

### Methods

`get_pokemon(args?)`: retrieves data about pokemon. If no arguments are passed, it will return ALL pokemon. Pass `id` or `name` to retrieve data about a specific pokemon.

- `args`
  - `id?`: retrieve pokemon by unique ID, optional
  - `name?`: retrieve pokemon by name, optional

`get_generaion(args?)`: retrieves data about pokemon generations. If no arguments are passed, it will return ALL generations. Pass `id` or `name` to retrieve data about a specific pokemon.

- `args`
  - `id?`: retrieves generation by unique ID, optional
  - `name`: retrieves generation by name, optional

## Examples

### 1. List the number of Generations

```
from pokemon_sdk import PokeAPI

client = PokeAPI()

generations = client.get_generation()

if generations:
    print(generations.count)
```

### Expected Result

```
9
```

### 2. Fetch specific Pokemon and extract a list of their moves

```
from pokemon_sdk import PokeAPI

client = PokeAPI()

pokemon = client.get_pokemon('bulbasaur')

if pokemon:
    name = pokemon.name
    moves = pokemon.moves
    moves_list = []

    for move in moves:
        moves_list.append(move['move']['name'])
    print(f"{name}'s moves: \n {moves_list}")

```

### Expected Result

```
bulbasaur's moves:
 ['razor-wind', 'swords-dance', 'cut', 'bind', 'vine-whip', 'headbutt', 'tackle', 'body-slam', 'take-down', 'double-edge', 'growl', 'strength', 'mega-drain', 'leech-seed', 'growth', 'razor-leaf', 'solar-beam', 'poison-powder', 'sleep-powder', 'petal-dance', 'string-shot', 'toxic', 'rage', 'mimic', 'double-team', 'defense-curl', 'light-screen', 'reflect', 'bide', 'sludge', 'skull-bash', 'amnesia', 'flash', 'rest', 'substitute', 'snore', 'curse', 'protect', 'sludge-bomb', 'mud-slap', 'outrage', 'giga-drain', 'endure', 'charm', 'false-swipe', 'swagger', 'fury-cutter', 'attract', 'sleep-talk', 'return', 'frustration', 'safeguard', 'sweet-scent', 'synthesis', 'hidden-power', 'sunny-day', 'rock-smash', 'facade', 'nature-power', 'helping-hand', 'ingrain', 'knock-off', 'secret-power', 'weather-ball', 'grass-whistle', 'bullet-seed', 'magical-leaf', 'natural-gift', 'worry-seed', 'seed-bomb', 'energy-ball', 'leaf-storm', 'power-whip', 'captivate', 'grass-knot', 'venoshock', 'acid-spray', 'round', 'echoed-voice', 'grass-pledge', 'work-up', 'grassy-terrain', 'confide', 'grassy-glide', 'tera-blast', 'trailblaze']
```

## Testing

Testing is included in the repo with [pytest](https://docs.pytest.org/en/stable/) and test script included in `tests/test_sdk.py`. Testing is not however included in the package via PIP. To run the integrations tests, clone the repo.

```
git clone https://github.com/PandaBacon21/pokeSDK.git
```

Once cloned, `cd` into that directory and install dependencies (again, I recommend using a virtual environment)

```
pip install -r requirements.txt
```

In the root directory run

```
pytest
```

or `pytest -v` for the detailed output

## Note

> This SDK uses Pydantic to validate API responses, ensuring the data matches the expected structure. It also allows access to response attributes using dot notation - `pokemon.moves` or `generation.count` for example. This makes it simple to extract specific attributes. However, further nested data, such as lists or dictionaries within these attributes still require bracket notation - `pokemon.moves['move']['name']` for example.

## License

This project is licensed under the MIT License and provided as is [LICENSE](LICENSE).
