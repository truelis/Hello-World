favorite_pizzas = ['pepperoni', 'hawaiian', 'veggie']
friend_pizzas = favorite_pizzas[:]

favorite_pizzas.append("meat")
friend_pizzas.append("margarita")

# print(f"\nMy favorite pizzas are:\n{favorite_pizzas}\n")
# print(f"\nMy friend's favorite pizzas are:\n{friend_pizzas}\n")

print(f"\nMy favorite pizzas are:")
for pizza in favorite_pizzas:
    print(pizza)

print(f"\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

