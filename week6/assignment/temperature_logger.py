# Temperature Logger (math module)
import math
 
station_name = "Kathmandu Weather Station"   # global variable
 
 
def get_average(temps):
    return sum(temps) / len(temps)
 
 
def get_deviation(temps):
    mean = get_average(temps)  # local variable, only exists inside this function
    variance = sum((t - mean) ** 2 for t in temps) / len(temps)
    return math.sqrt(variance)
 
 
def get_summary(temps):
    print(f"--- {station_name} ---")
    print(f"Min: {min(temps)}")
    print(f"Max: {max(temps)}")
    print(f"Average: {get_average(temps):.2f}")
    print(f"Deviation: {get_deviation(temps):.2f}")
 
 
temperatures = [18.4, 22.1, 15.7, 29.3, 11.8, 25.6, 19.2]
get_summary(temperatures)
 

