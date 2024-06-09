prompt = "What topping would you like? "
prompt += "Enter quit when you finish: "

# toppings = []
while True:
    topping = input(prompt)
    
    if topping.lower() != 'quit':
        print(f"I am adding {topping} to your toppings")
        # toppings.append(prompt)
    else:
        break