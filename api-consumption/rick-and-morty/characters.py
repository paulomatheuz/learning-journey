import requests


def fetch_data(endpoint, filters=None):
    url = f"https://rickandmortyapi.com/api/{endpoint}"
    response = requests.get(url, params=filters, timeout=10)

    return response.json() if response.status_code == 200 else None


for name in ["Rick", "Morty", "Evil Morty"]:
    characters = fetch_data("character", {"name": name})

    if characters and characters["results"]:
        character = characters["results"][0]

        print(f"Nome: {character['name']}")
        print(f"Status: {character['status']}")
        print(f"Espécie: {character['species']}")
        print(f"Origem: {character['origin']['name']}")
        print("-" * 40)
    else:
        print(f"Failed to fetch data.")