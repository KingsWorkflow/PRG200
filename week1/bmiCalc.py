# BMI Calculator for Health Camp
weight = float(input("Enter weight in kg: "))
height_cm = float(input("Enter height in cm: "))

height_m = height_cm / 100  # Convert cm to meters
bmi = weight / (height_m ** 2)

print(f"\n--- BMI Summary ---")
print(f"Weight: {weight:.1f} kg")
print(f"Height: {height_cm:.1f} cm ({height_m:.2f} m)")
print(f"BMI: {bmi:.1f}")