import requests


def fetch_data(endpoint, filters=None):
    url = f"https://thesimpsonsapi.com/api/{endpoint}"
    response = requests.get(url, params=filters, timeout=10)

    return response.json() if response.status_code == 200 else None


for name in ["Bart", "Homer", "Maggie", "Lisa", "Marge"]:
    page = 1

    while True:
        characters = fetch_data("characters", {"page": page})

        if not characters:
            print(f"Falha ao buscar dados de {name}")
            break

        for item in characters["results"]:
            character = item
            break

        if character or not characters["next"]:
            break

        page += 1

    if character:
        print(f"Name: {character['name']}")
        print(f"Age: {character['age']}")
        print(f"Occupation: {character['occupation']}")
        print(f"Status: {character['status']}")
        print("-" * 30)
    elif characters is not None:
        print(f"Personagem não encontrado: {name}")