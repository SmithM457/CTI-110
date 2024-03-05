#Matthew Howe
#3/5/24
#P2LAB2
#Create a dictionary and use codes to pull information from the dictionary

car_dict = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
    }
car_list = car_dict
print("The keys in the dictionary are: ")
print(*car_list, sep=", ")
print()
vehicle = input("Enter a vehicle to see it mpg: ")
print()
mpg = car_dict.get(vehicle)
print("The " + vehicle + " gets",mpg,"mpg.")
print()
miles = float(input("How many miles will drive the " + vehicle + "? "))
print()
gallons = miles/mpg
print(f'{gallons:.2f} gallon(s) of gas are needed to drive the {vehicle} {miles:.1f} miles.')

