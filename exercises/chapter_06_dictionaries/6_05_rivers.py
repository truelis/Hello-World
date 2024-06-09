rivers ={
    'Neil': 'Egypt',
    'Thames': 'UK',
    'Kifisos': 'Greece'
    }
print("   Rivers And Countries")
for river,country in rivers.items():
    print(f"\nThe {river} river runs through:\n{country}")

# extra line in the end for readability
print("\n")

print("   Only Rivers Names")
for river in rivers.keys():
    print(f"{river}")

# extra line in the end for readability
print("\n")
print("   Only Country Names")
for country in rivers.values():
    print(f"{country}")

