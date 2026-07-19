# Password Strength Checker
passwords = ["hello", "Hello123", "H3ll0@World", "12345678", "MyP@ss!"]
special_characters = "!@#$%^&*"
 
for pwd in passwords:
    missing = []
 
    if len(pwd) < 8:
        missing.append("at least 8 characters")
    if not any(ch.isupper() for ch in pwd):
        missing.append("an uppercase letter")
    if not any(ch.islower() for ch in pwd):
        missing.append("a lowercase letter")
    if not any(ch.isdigit() for ch in pwd):
        missing.append("a digit")
    if not any(ch in special_characters for ch in pwd):
        missing.append("a special character (!@#$%^&*)")
 
    if missing:
        print(f"{pwd}: WEAK - Missing: {', '.join(missing)}")
    else:
        print(f"{pwd}: STRONG")
