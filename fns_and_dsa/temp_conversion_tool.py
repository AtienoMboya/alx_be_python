FARENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FARENHEIT_FACTOR = 9/5

def convert_to_celsius(farenheit):
    return farenheit * FARENHEIT_TO_CELSIUS_FACTOR

def convert_to_farenheit(celsius):
    return celsius * CELSIUS_TO_FARENHEIT_FACTOR

temperature = input("Enter the temperature to convert: ")
unit = input("Is this temperature in Celsius or Farenheit? (C/F): ").upper()

if temperature.isdigit():
    if unit == 'F':
        print(f'{float(temperature)}°F is {convert_to_celsius(float(temperature))}°C')
    else:
        print(f'{float(temperature)}°C is {convert_to_farenheit(float(temperature))}°F')
else:
    print("Invalid temperature. Please enter a numeric value")
