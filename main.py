"""
Initializing variables and getting input
"""
#vehicle_type = input("Enter the vehicle type: ")
#fuel_prices = input("Enter the price of fuel: ") # funct to fetch online info 
# have a function to scrap the internet to check current fuel prices 
# or else use the default

def get_input(prompt: str, valid_options: list = None):
    """
    Function to fetch user input from the user
    Args:
        prompt: string stating the input to be fetched
        valid_options: list with acceptable choices
    """
    while True:
        user_input = input(prompt).strip().lower()
        if valid_options and user_input not in valid_options:
            print (f"Invalid choice. Kindly choose between the following options:\n{', '.join(valid_options)}.")
        else:
            return user_input


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


def fuel_type():
    """
    Function to determine the type of fuel
    """
    fuel_type = get_input("Enter the type of fuel: \na)Petrol \nb)Diesel \nEnter either (a) or (b): ", ['a', 'b'])
    return fuel_type


def total_cost(total_liters, fuel_type):
    """
    Function to calculate total cost
    Args:
        total_liters: number of liters to be used in travel
        fuel_type: type of fuel, either diesel or petrol
    """
    if fuel_type == 'a':
        price_per_liter = 188
    else:
        price_per_liter = 170

    total_price = total_liters * price_per_liter
    return total_price

def main():
    distance_to_be_covered = float(get_input("Enter the distance to be travelled: "))
    car_type = get_input("Enter the type of car to be used: \na) Sedan \nb) SUV \nc) Truck \nEnter either (a), (b), or (c): ", ['a', 'b', 'c'])
    avg_fuel_consumption = float(get_input("Enter the average consumption of the vehicle to be used: "))
    fuel_type_var = fuel_type()
    total_fuel = ttl_fuel_consumption(distance_to_be_covered, avg_fuel_consumption)
    final_price = total_cost(total_fuel, fuel_type_var)
    print(f"The total litres to be consumed {total_fuel}. \nThe total amount to be spent is {final_price}")

if __name__ == "__main__":
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
