# Age Calculator (BS Birth Year)
birth_year = int(input("Enter your birth year (BS): "))
current_year = int(input("Enter current BS year: "))

age = current_year - birth_year

print(f"\n--- Age Summary ---")
print(f"Birth year (BS): {birth_year}")
print(f"Current year (BS): {current_year}")
print(f"Your age is: {age} years old")