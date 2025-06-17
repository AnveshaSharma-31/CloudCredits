def calculate_bmi(weight, height):
    return weight / (height ** 2)

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("Welcome to BMI Calculator!")
    
    unit_system = input("Choose unit system: Metric (M) or Imperial (I): ").strip().upper()
    
    if unit_system == 'M':
        height = float(input("Enter your height in meters (e.g., 1.75): "))
        weight = float(input("Enter your weight in kilograms (e.g., 68): "))
    elif unit_system == 'I':
        height_feet = float(input("Enter your height - feet part (e.g., 5): "))
        height_inches = float(input("Enter your height - inches part (e.g., 9): "))
        weight = float(input("Enter your weight in pounds (e.g., 150): "))
        
        # Convert height to meters
        total_inches = height_feet * 12 + height_inches
        height = total_inches * 0.0254
        
        # Convert weight to kilograms
        weight = weight * 0.453592
    else:
        print("Invalid unit system selected.")
        return
    
    bmi = calculate_bmi(weight, height)
    category = interpret_bmi(bmi)
    
    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"Category: {category}")

if __name__ == "__main__":
    main()
