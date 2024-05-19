guest_list = ["Bill Gates", "Elon Musk", "Gio", "Vagias", "Spiros"]
print(guest_list)

guest_list.remove("Gio")


spiros_index = guest_list.index("Spiros")
guest_list[spiros_index] = "Antonis"

print("\nThere are going to be more seats available")

guest_list.insert(0, "Kostas")
guest_list.insert(2, "Miltos")
guest_list.append("Haris")
for guest in guest_list:
    print(f"\nCan you come in my wedding {guest}?")