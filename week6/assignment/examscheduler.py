# Exam Scheduler (datetime module)
import datetime
 
college_name = "Bhaktapur Multiple Campus"   # global variable
 
 
def parse_date(date_str):
    return datetime.datetime.strptime(date_str, "%Y-%m-%d")
 
 
def get_exam_date(start_str, days):
    start = parse_date(start_str)
    exam_date = start + datetime.timedelta(days=days)
    return exam_date.strftime("%Y-%m-%d")
 
 
def print_schedule(start_str, exams):
    print(f"--- {college_name} Exam Schedule ---")
    for subject, days in exams:
        date_str = get_exam_date(start_str, days)
        print(f"{subject}: {date_str}")
 
 
start_date = "2025-05-01"
exams = [
    ("Python Programming", 0),
    ("Data Structures", 3),
    ("Database Systems", 6),
    ("Computer Networks", 10),
    ("Mathematics", 14),
]
print_schedule(start_date, exams)
