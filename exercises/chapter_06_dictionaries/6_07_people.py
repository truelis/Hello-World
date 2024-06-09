friend_1 = {
    'first_name':'spiros',
    'last_name':'atmatzidis',
    'age':'37',
    'city':'Athens'
    }

friend_2 = {
    'first_name':'panagiotis',
    'last_name':'vagias',
    'age':'37',
    'city':'Athens'
    }

friend_3 = {
    'first_name':'giorgos',
    'last_name':'armodoros',
    'age':'37',
    'city':'Athens'
    }
people = [friend_1, friend_2, friend_3]

# n = 0
for friend in people:
    # n+=1
    print(f"My friend's name is {friend['first_name'].title()} {friend['last_name'].title()}. " 
          f"They are {friend['age']} years old and they live in {friend['city']} ")


