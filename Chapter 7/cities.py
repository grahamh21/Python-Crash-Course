prompt = 'Say the name of a city you have visited this year:\n'
prompt += "Enter 'quit' to stop."

active = True
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("\nI sure would love to visit " + city.title() + ' someday!')

#A loop that starts with while True will run forever unless it reaches a break
#statement
