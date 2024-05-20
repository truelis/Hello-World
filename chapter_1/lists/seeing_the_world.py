destination_list = ["Iceland", "Norway", "Greece", "Spain", "Germany"]

print(f"\n{destination_list}")

print(f"\nThis should be a shorted list:",f"\n",sorted(destination_list))

print(f"\nThe original list is still unsorted:\n{destination_list}")

print(f"\nThis is shorted in reverse\n",sorted(destination_list, reverse=True))

print(f"\nThe original list is still unsorted:\n{destination_list}\n")

destination_list.reverse()

print(f"\nThe list reversed:\n{destination_list}\n")

destination_list.reverse()

print(f"\nThe list reversed again:\n{destination_list}\n")

destination_list.sort()

print(f"\nThe list sorted:\n{destination_list}\n")

destination_list.sort(reverse=True)

print(f"\nThe list sorted in reverse:\n{destination_list}\n")