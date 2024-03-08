try:
    np_weight = float(input("Enter your weight: "))
    np_height = float(input("Enter your height in cm: ")) / 100  # Convert height to meters
except ValueError:
    print("Please enter valid numeric values for weight and height")
    exit()

# Calculate bmi
bmi = np_weight / np_height ** 2

# Print the result
print("Your BMI is:", bmi)
