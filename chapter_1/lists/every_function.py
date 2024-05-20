things_to_buy = ["chair", "sofa", "plates", "table"]

print(f"\nOriginal list:\n{things_to_buy}")

things_to_buy.append("desk")

print(f"\nAppended list:\n{things_to_buy}")

print("\n           The list sorted:\n          ",sorted(things_to_buy))

print(f"\nOriginal list still unsorted:\n{things_to_buy}\n")

# Sort and stick
things_to_buy.sort()
print(f"\nOriginal list now permanently sorted:\n{things_to_buy}\n")

# Reverse the list
things_to_buy.reverse()
print(f"\nThe list reversed:\n{things_to_buy}\n")

# Pop something and print it while also print the list
things_to_buy.pop(0)
print(f"\nOriginal list popped in place 0:\n{things_to_buy}\n")

# Remove an item from the list and print the list
things_to_buy.remove("sofa")
print(f"\nOriginal list still with sofa removed:\n{things_to_buy}\n")

# Delete an item with delete that removes with index and print the list
del things_to_buy[0]
print(f"\nOriginal list with deletion of index 0:\n{things_to_buy}\n")





