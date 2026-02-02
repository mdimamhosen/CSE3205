
def thermostat_agent(temperature):
    """
    Simple Reflex Agent that controls a heater based on temperature.
    """
    if temperature < 20:
        return "Heater ON"
    else:
        return "Heater OFF"

def main():
    try:
        temp = float(input("Enter the current temperature (°C): "))
        action = thermostat_agent(temp)
        print("Action:", action)
    except ValueError:
        print("Invalid input! Please enter a numeric value.")

if __name__ == "__main__":
    main()
