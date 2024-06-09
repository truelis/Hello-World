favorite_places = {
    'giorgos': ['athens', 'london', 'sydney'],
    'panos': ['athens', 'bali', 'tokyo'],
    'spiros': ['athens', 'milan', 'istanbul']
}

for person,places in favorite_places.items():
    print(f"\n{person.title()} has", len(places), f"favorite places. These are:")
    for place in places:
        print(place.title())
          
