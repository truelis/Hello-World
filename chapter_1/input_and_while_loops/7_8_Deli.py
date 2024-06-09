sandwitch_orders = ['chicken', 'tuna', 'steak', 'vegan']

finished_sandwitches = []

while sandwitch_orders:
    current_sandwitch = sandwitch_orders.pop()
    print(f"I am now making the {current_sandwitch} sandwitch")
    finished_sandwitches.append(current_sandwitch)

print("\n")

for sandwitch in finished_sandwitches:
    print(f"Your {sandwitch} sandwitch is ready")

