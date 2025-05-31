print("=== Body Temperature Checker ===")

try:
    temperature = float(input("Enter your body temperature in °C: "))

    if temperature > 37.5:
        print("You might have a fever. Please take care!")
    elif temperature < 35.0:
        print("Your temperature is low. Stay warm and rest.")
    else:
        print("Your temperature is normal.")
except ValueError:
    print("Please enter a valid number.")
