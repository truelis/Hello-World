current_users = ['Dimi', 'Kostas', 'Andonis', 'Giannis', 'Paulos']

new_users = ['DIMI', 'kostas', 'vlassis', 'hristos', 'spiros']

current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())

print("\n")
for user in new_users:
    if user.lower() in current_users_lower:
        print(f"You must select a new username as the {user} is taken")
    else:
        print(
            f"Nice username {user}! "
            "You can use this username as nobody"
            " else is already using it."
        )

print("\n")
