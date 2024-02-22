##Matthew Howe
##2/22/24
##P1HW2
##This program calculates and displays travel expenses

print("This program calculates and displays travel expenses")
print("")
budget = int(input("Enter Budget: "))
print("")
location = input("Enter your travel destination: ")
print("")
gas = int(input("How much do you think you will spend on gas? "))
print("")
hotel = int(input("Approximately, how much will you need for accomodation/hotel? "))
print("")
food = int(input("Lastly, how much do you need for food? "))
print("")
print("------------Travel Expenses------------")
print("Location: "+ str(location) + '.')
print("Initial Budget: ",budget)
print("")
print("Fuel: ",gas)
print("Accomodation: ",hotel)
print("Food: ",food)
print("")
balance = budget - gas - hotel - food
print("Remaining Balance: ",balance)

##Pseudocode
##get budget
##get location
##get gas
##get hotel
##get food
##print location
##print initial budget
##print fuel
##print accomodation
##print food
##calculate and display final balance
