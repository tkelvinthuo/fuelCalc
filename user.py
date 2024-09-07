import PySimpleGUI as sg

# Constants for fuel prices
PETROL_PRICE_PER_LITER = 188
DIESEL_PRICE_PER_LITER = 170

def calculate_total_fuel_consumption(distance: float, avg_fuel_consumption: float) -> float:
    """
    Calculate the total amount of fuel required for a given distance and fuel consumption rate.
    Args:
        distance (float): Distance to be covered.
        avg_fuel_consumption (float): Average fuel consumption of the vehicle (liters per km).
    Returns:
        float: Total fuel required in liters.
    """
    total_liters = distance / avg_fuel_consumption
    return total_liters

def calculate_total_cost(fuel_liters: float, fuel_type: str) -> float:
    """
    Calculate the total cost of fuel for a given amount and fuel type.
    Args:
        fuel_liters (float): Total fuel required in liters.
        fuel_type (str): Type of fuel ('a' for Petrol, 'b' for Diesel).
    Returns:
        float: Total cost of the fuel.
    """
    if fuel_type == 'Petrol':
        price_per_liter = PETROL_PRICE_PER_LITER
    else:  # Diesel
        price_per_liter = DIESEL_PRICE_PER_LITER

    total_cost = fuel_liters * price_per_liter
    return total_cost

def main():
    """
    Main function to create a GUI for calculating fuel consumption and cost.
    """
    # Define the window layout
    layout = [
        [sg.Text('Enter the distance to be travelled (in km):'), sg.InputText(key='-DISTANCE-')],
        [sg.Text('Select the type of car to be used:'), sg.Combo(['Sedan', 'SUV', 'Truck'], key='-CAR_TYPE-')],
        [sg.Text('Enter the average consumption of the vehicle (liters per km):'), sg.InputText(key='-AVG_CONSUMPTION-')],
        [sg.Text('Select the type of fuel:'), sg.Combo(['Petrol', 'Diesel'], key='-FUEL_TYPE-')],
        [sg.Button('Calculate'), sg.Button('Exit')],
        [sg.Text('Total fuel to be consumed (liters):'), sg.Text('', key='-TOTAL_FUEL-')],
        [sg.Text('Total amount to be spent on fuel:'), sg.Text('', key='-TOTAL_COST-')]
    ]

    # Create the window
    window = sg.Window('Fuel Cost Calculator', layout)

    # Event loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break

        if event == 'Calculate':
            try:
                # Get input values from the GUI
                distance = float(values['-DISTANCE-'])
                avg_fuel_consumption = float(values['-AVG_CONSUMPTION-'])
                fuel_type = values['-FUEL_TYPE-']

                # Validate input
                if not fuel_type:
                    sg.popup('Please select a fuel type.')
                    continue

                # Calculate total fuel and cost
                total_fuel = calculate_total_fuel_consumption(distance, avg_fuel_consumption)
                final_price = calculate_total_cost(total_fuel, fuel_type)

                # Update the results in the GUI
                window['-TOTAL_FUEL-'].update(f'{total_fuel:.2f} liters')
                window['-TOTAL_COST-'].update(f'{final_price:.2f} currency units')

            except ValueError:
                sg.popup('Please enter valid numerical values for distance and average consumption.')

    window.close()

if __name__ == "__main__":
    main()

