# Student Enrollment Profile
def build_profile(name, **details):
    print(f"Name: {name}")
    for key, value in details.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
 
 
# Test calls
build_profile("Prashanna", program="BSCS", portfolio="github.com/pd")
print()
build_profile("Sita", program="BBA")
