print("=== Body Temperature Checker ===")

while True:
    try:
        temperature = float(input("Enter your body temperature in °C (or type 'q' to quit): "))
        
        if temperature > 37.5:
            print("You might have a fever. Please take care!")
        elif temperature < 35.0:
            print("Your temperature is low. Stay warm and rest.")
        else:
            print("Your temperature is normal.")
            
    except ValueError:
        print("Please enter a valid number.")
        continue

    # Ask if user wants to check again
    again = input("Check another temperature? (y/n): ").strip().lower()
    if again != 'y':
        print("Goodbye!")
        break
