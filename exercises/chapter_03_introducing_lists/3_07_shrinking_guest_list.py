guest_list = ["Bill Gates", "Elon Musk", "Gio", "Vagias", "Spiros"]
print(guest_list)

print("\nThere are not going to be more than two seats available")


bill_gates_index = guest_list.index("Bill Gates")
guest_list[bill_gates_index] = "Antonis"

for i in range(3):
    removed_guest = guest_list.pop()
    print(f"\n\nSorry but I cannot invite you {removed_guest}\n")

for guest in guest_list:
    print(f"\nYou are still invited {guest}\n")

del guest_list[0]
del guest_list[0]

print(guest_list)


# guest_list.insert(0, "Kostas")
# guest_list.insert(2, "Miltos")
# guest_list.append("Haris")
# for guest in guest_list:
#     print(f"\nCan you come in my wedding {guest}?")