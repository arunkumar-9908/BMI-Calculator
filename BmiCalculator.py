def calculate_bmi(weight, height):
    return weight / (height ** 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("❗ Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("❗ Invalid input. Please enter a number.")

def main():
    print("🧮 Welcome to the BMI Calculator")
    while True:
        weight = get_positive_float("Enter your weight in kilograms (kg): ")
        height = get_positive_float("Enter your height in meters (m): ")
        
        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)

        print(f"\n📊 Your BMI is: {bmi:.2f}")
        print(f"📌 Category: {category}")

        again = input("\n🔁 Do you want to calculate again? (y/n): ").strip().lower()
        if again != 'y':
            print("👋 Goodbye! Stay healthy.")
            break

if __name__ == "__main__":
    main()
