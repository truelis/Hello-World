name_promt = "\nWhat's your name?"
country_promt = "If you could visit one place in the world what would it be? "
break_promt = "Is there anybody you would like to respond (yes/no) "

#Responses of the poll will be stored in a dictionary
responses = {}

while True:
    name = input(name_promt)
    country = input(country_promt)

    #Store each response
    responses[name] = country
        
    #Break if the answer was no
    exit_or_not = input(break_promt)
    if exit_or_not == 'no':
        break

#Print the reults of the poll
print("\n---Results---")
for name,country in responses.items():
    print(f"{name.title()} would like to visit {country.title()}")

