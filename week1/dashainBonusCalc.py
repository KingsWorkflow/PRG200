# Dashain Bonus Calculator
monthly_salary = float(input("Enter monthly basic salary (Rs): "))
deduction_percent = float(input("Enter income-related deduction percentage: "))

bonus = monthly_salary  # One month's salary as bonus
deduction = bonus * (deduction_percent / 100)
take_home_bonus = bonus - deduction

print(f"\n--- Dashain Bonus Summary ---")
print(f"Monthly salary: Rs. {monthly_salary:.2f}")
print(f"Gross bonus: Rs. {bonus:.2f}")
print(f"Deduction ({deduction_percent}%): Rs. {deduction:.2f}")
print(f"Final take-home bonus: Rs. {take_home_bonus:.2f}")