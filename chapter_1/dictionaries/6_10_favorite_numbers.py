friends_and_favorite_numbers = {
    'kostas': [5,6,7],
    'antonis': [4,22,44],
    'giorgos': [3,56,78],
    'dimitris': [7,98,23],
    'spiros': [10,878,568],
}

for person,numbers in friends_and_favorite_numbers.items():
    if person[-1] == 's':
        print(f"{person.title()}' favorite numbers are:")
    else:
        print(f"{person.title()}'s favorite numbers are:")
    for number in numbers:
        print(number)

