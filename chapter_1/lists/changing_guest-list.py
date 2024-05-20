guest_list = ["Bill Gates", "Elon Musk", "Gio", "Vagias", "Spiros"]
print(guest_list)

guest_list.remove("Gio")

print(f"\nThis is the new list with a person removed: \n{guest_list}")

spiros_index = guest_list.index("Spiros")
guest_list[spiros_index] = "Antonis"

print(f"This is the list after replacing spiros: \n{guest_list}")

for guest in guest_list:
    print(f"Can you come in my wedding {guest}?")