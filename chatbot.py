#5. Develop an elementary chatbot for any suitable customer interaction application.
# As they have mentioned 'elementary' in the problem statements it has to be hardcoded statement based still staticness can be removed using dynamic reponses with storage structures
# Any if else based solution is a valid solution to this practical as they have mentioned in the statement as 'elementary' chatbot
import re
# storage structures can be used to generate dynamic reponses can be replaced with db , external world
groceries = {
    'apple': {'name': 'Apple', 'price': 199, 'unit': 'per Kg'},
    'banana': {'name': 'Banana', 'price': 99, 'unit': 'per Kg'},
    'milk': {'name': 'Milk', 'price': 49, 'unit': 'per Liter'}
}

# mapper for 'wh' type questions to reduce if else ladder ;
property_functions = {
    'price': lambda item: item.get('price', f"I don't have information about the price of {item['name']}."),
    'unit': lambda item: item.get('unit', f"I don't have information about the unit of {item['name']}.")
}

# Regular expression to match statements
statement_pattern = re.compile(r"what is the (\w+) of (\w+)\??")

while True:

    statement = input("What would you like to know? \nyou :").lower()
    #During The practical Any related if statements can be inserted here
    #eg
    #if statement == "Wheres the stores location":
        #print("Yerwada,Pune")
        #break

    if statement.lower() == "exit":
        break

    # Use regular expression to extract property and name
    match = statement_pattern.match(statement)
    if match:
        property_name = match.group(1).lower()
        name = match.group(2)
        if name in groceries:
            item = groceries[name]
            if property_name in property_functions:
                value = property_functions[property_name](item)
                print(f"The {property_name} of {name} is {value}")
            else:
                print(f"I don't know about {property_name}.")
        else:
            print(f"I don't have information about {name}.")
    else:
        print("Sorry, I don't understand. Please ask me again.")


#accepts response in the format what is the (price or unit) of (any product)
#what is the price of apple
#what is the unit of list
