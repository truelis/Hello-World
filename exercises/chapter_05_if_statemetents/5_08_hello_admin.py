usernames = ['admin', 'truelis', 'gio', 'spiros', 'vagias']

for username in usernames:
    if username == 'admin':
      print(f"\nHello admin, would you like to see a status report?")
    else:
        print(f"Hello {username.title()}, thank you for logging in again")
