favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

people_to_take_the_poll = ['jen', 'edward', 'antonis', 'spiros']

for name in people_to_take_the_poll:
    if name in favorite_languages.keys():
        print(f"Thank you for taking the poll {name.title()}")
    else:
        print(f"Please vote your favorite programming language {name.title()}")

    