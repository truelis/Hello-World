prompt = "What is your age? "
prompt += "\nWhen you finish enter 'quit': "

while True:
    age = input(prompt)

    if age.lower() == 'quit':
        break
    age = float(age)
    if age < 3:
        print("The entrance is free")
    elif age >=3 and age <=12:
        print("The price is £10")
    else:
        print("The price is £15")
        
