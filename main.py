"""
Initializing variables and getting input
"""
#vehicle_type = input("Enter the vehicle type: ")
#fuel_prices = input("Enter the price of fuel: ") # funct to fetch online info 
# have a function to scrap the internet to check current fuel prices 
# or else use the default
def ttl_fuel_consumption(d_covered, avg_fuel_cons):
    """
    Function to calculate the total amount of fuel that will be used
    Args:
        d_covered: distance to be covered
        avg_fuel_cons: average fuel consumption for each car
    """
    total_in_liters = int(d_covered) / int(avg_fuel_cons)
    print(total_in_liters)
    return (total_in_liters)

#ttl_fuel_consumption(distance_to_be_covered, avg_fuel_consumption)

def fuel_type():
    fuel_type = input("Enter the type of fuel: \na)Petrol \nb)Diesel \nEnter either (a) or (b): ")
    return fuel_type
def ttl_price(ttl_liters, fuel_type):
    if fuel_type == 'a':
        price_per_liter = 188
    else:
        price_per_liter = 170

    total_price = ttl_liters * price_per_liter
    return total_price

def main():
    distance_to_be_covered = input("Enter the distance to be travelled: ")
    car_type = input("Enter the type of car to be used: \na) Sedan \nb) SUV \nc) Truck \nEnter either (a), (b), or (c): ")
    avg_fuel_consumption = input("Enter the average consumption of the vehicle to be used: ")
    fuel_type_var = fuel_type()
    total_fuel = ttl_fuel_consumption(distance_to_be_covered, avg_fuel_consumption)
    final_price = ttl_price(total_fuel, fuel_type_var)
    print(f"The total litres to be consumed {total_fuel}. \nThe total amount to be spent is {final_price}")

main()

"""
Pseudocode
1. INPUT from the user about three items:
    a) Distance to be travelled
    b) Type of car
    c) Type of fuel to be used
    d) Avg fuel consumption
2. Calculate the max litres to be consumed
3. Calculate the value in money value
4. PRINT to the user
5. Add user interface
6. Save the data to a file storage as the database
"""
