def temperature():
    user = float(input("Enter temperature: "))
    source_unit = input("Enter the unit of Temperature: ")
    target_unit = input("Enter the unit of temperature to convert in: ")
    temp = 0
    
    if source_unit.lower() == "celsius" and target_unit.lower() == "fahrenheit":
        temp = (user * 1.8 + 32)
    elif source_unit.lower() == "celsius" and target_unit.lower() == "kelvin":
        temp = user + 273.15
    elif source_unit.lower() == "fahrenheit" and target_unit.lower() == "celsius":
        temp = (user - 32) * 5 / 9
    elif source_unit.lower() == "fahrenheit" and target_unit.lower() == "kelvin":
        temp = (user - 32) * 5/9 + 273.15
    elif source_unit.lower() == "kelvin" and target_unit.lower() == "celsius":
        temp = user - 273.15
    elif source_unit.lower() == "kelvin" and target_unit.lower() == "fahrenheit":
        temp = (user - 273.15) * 9.0 / 5.0 + 32.0
    else:
        return "Invalid units!!!"
    
    return f"{user} {source_unit} is equals to {temp} {target_unit}."

def distance():
    user = float(input("Enter distance: "))
    source_unit = input("Enter the unit of distance: ").strip().lower()
    target_unit = input("Enter the desired unit to be converted: ").strip().lower()
    dist = 0
    if source_unit == "m" and target_unit == "km":
        dist = user / 1000
    elif source_unit == "m" and target_unit == "cm":
        dist = user * 100
    elif source_unit == "m" and target_unit == "miles":
        dist = user * 0.000621371192
    elif source_unit == "km" and target_unit == "m":
        dist = user * 1000
    elif source_unit == "km" and target_unit == "cm":
        dist = user * 100000
    elif source_unit == "km" and target_unit == "miles":
        dist = user * 0.621371
    elif source_unit == "cm" and target_unit == "m":
        dist = user / 100
    elif source_unit == "cm" and target_unit == "km":
        dist = user / 100000
    elif source_unit == "cm" and target_unit == "miles":
        dist = user * 0.00000621371
    elif source_unit == "miles" and target_unit == "m":
        dist = user * 1609.344
    elif source_unit == "miles" and target_unit == "km":
        dist = user * 1.609344
    elif source_unit == "miles" and target_unit == "cm":
        dist = user * 160934.4
    else:
        return "Invalid units!!!"
    
    return f"{user} {source_unit} is equals to {dist} {target_unit}."

def weight():
    user = float(input("Enter weight: "))
    source_unit = input("Enter unit of weight: ")
    target_unit = input("Enter unit of weight to convert in: ")
    weight = 0
    if source_unit.lower() == "grams" and target_unit.lower() == "kg":
        weight = user / 1000
    elif source_unit.lower() == "grams" and target_unit.lower() == "pounds":
        weight = user / 453.5923
    elif source_unit.lower() == "kg" and target_unit.lower() == "grams":
        weight = user * 1000
    elif source_unit.lower() == "kg" and target_unit.lower() == "pounds":
        weight = user * 2.2046226218
    elif source_unit.lower() == "pounds" and target_unit.lower() == "grams":
        weight = user * 453.59237
    elif source_unit.lower() == "pounds" and target_unit.lower() == "kg":
        weight = user * 0.45359237
    else:
        return "Invalid units!!!"
    
    return f"{user} {source_unit} is equals to {weight} {target_unit}"

while True:
    print("===== UNIT CONVERTER =====")
    print("\n1. Temperature\n2. Distance\n3. Weight\n4. Exit\n")
    choice = input("Enter your choice: ")
    
    if choice == "1" or choice.lower() == "temperature":
        print(temperature())
    elif choice == "2" or choice.lower() == "distance":
        print(distance())
    elif choice == "3" or choice.lower() == "weight":
        print(weight())
    elif choice == "4" or choice.lower() == "exit":
        break
    else:
        print("Invalid choice")