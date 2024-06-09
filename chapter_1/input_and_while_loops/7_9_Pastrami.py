sandwitch_orders = ['chicken', 'pastrami','tuna', 'pastrami', 'steak', 'vegan', 'pastrami']

finished_sandwitches = []
    
print("\nThe deli has run out of pastrami\n")

while 'pastrami' in sandwitch_orders:
    sandwitch_orders.remove('pastrami')

# Removing pastrami sandwitches but with a for loop instead of while
# for sandwitch in sandwitch_orders:
#     if sandwitch == 'pastrami':
#         sandwitch_orders.remove('pastrami')
    

while sandwitch_orders:
    current_sandwitch = sandwitch_orders.pop()
    print(f"I am now making the {current_sandwitch} sandwitch")
    finished_sandwitches.append(current_sandwitch)

print("\n")

for sandwitch in finished_sandwitches:
    print(f"Your {sandwitch} sandwitch is ready")

