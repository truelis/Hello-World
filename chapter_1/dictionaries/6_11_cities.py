cities = {
    'Athens': {
        'country': 'Greece',
        'population': '4M',
        'fact': 'the capital'
    },
    'Thessaloniki': {
        'country': 'Greece',
        'population': '2M',
        'fact': 'the 2nd biggest city'
    },
    'Piraias': {
        'country': 'Greece',
        'population': '1M',
        'fact': 'the 3rd biggest city'
    } 
}

for city,information in cities.items():
    print(f"{city.title()} belongs to {information['country'].title()}. "
          f"It has a population of {information['population']}, "
          f"and it is {information['fact']}")
    