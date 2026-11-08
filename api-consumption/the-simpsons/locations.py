import requests


def fetch_data(endpoints, filters=None):
    url = f"https://thesimpsonsapi.com/api/{endpoints}"
    response = requests.get(url, params=filters, timeout=10)

    return response.json() if response.status_code == 200 else None


for name in ["Krusty Burger", "Moe's Tavern", "Duff Brewery"]:
    page = 1
    location = None

    while True:
        locations = fetch_data("locations", {"page": page})

        if locations is None:
            print(f"Falha ao buscar dados de {name}")
            break

        for item in locations["results"]:
            if name.lower() in item["name"].lower():
                location = item
                break

        if location or not locations["next"]:
            break

        page += 1

    if location:
        print(f"Local: {location['name']}")
        print(f"Cidade: {location.get('town') or 'Não informada'}")
        print("-" * 40)
    elif locations is not None:
        print(f"Local não encontrado: {name}")