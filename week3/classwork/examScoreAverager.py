# Exam Score Averager
def average_score(*marks):
    if len(marks) == 0:
        return 0
    return sum(marks) / len(marks)
 
 
# Test calls
print(f"Average of 3 subjects: {average_score(78, 85, 92):.2f}")
print(f"Average of 5 subjects: {average_score(70, 65, 80, 90, 60):.2f}")
