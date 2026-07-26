# Date Converter for Nepal Bank System (BS <-> AD)
# Note: only the year is shifted per the formula given in the assignment;
# month/day are carried over unchanged and only reformatted per 'style'.
bs_months = ["Baisakh", "Jestha", "Ashadh", "Shrawan", "Bhadra", "Ashwin",
             "Kartik", "Mangsir", "Poush", "Magh", "Falgun", "Chaitra"]
ad_months = ["January", "February", "March", "April", "May", "June", "July",
             "August", "September", "October", "November", "December"]
 
 
def ordinal_suffix(n):
    if 11 <= n % 100 <= 13:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return f"{n}{suffix}"
 
 
def convert_date(date_str, from_cal, to_cal, style="iso"):
    year, month, day = map(int, date_str.split("-"))
 
    if from_cal == to_cal:
        converted_year = year
    elif from_cal == "AD" and to_cal == "BS":
        converted_year = year + 56
    elif from_cal == "BS" and to_cal == "AD":
        converted_year = year - 56
    else:
        raise ValueError("Unsupported calendar conversion")
 
    month_name = (bs_months if to_cal == "BS" else ad_months)[month - 1]
 
    if style == "iso":
        return f"{converted_year:04d}-{month:02d}-{day:02d} {to_cal}"
    elif style == "full":
        return f"{ordinal_suffix(day)} {month_name}, {converted_year} {to_cal}"
    elif style == "nepali":
        return f"{day} {month_name}, {converted_year} {to_cal}"
    else:
        return f"{converted_year:04d}-{month:02d}-{day:02d} {to_cal}"
 
 
customers = [
    {"name": "Ramesh Thapa", "date": "1985-06-24", "cal": "AD", "need": "BS", "style": "full"},
    {"name": "Sunita Karki", "date": "2055-09-10", "cal": "BS", "need": "AD", "style": "iso"},
    {"name": "Bikash Rai", "date": "1998-11-30", "cal": "AD", "need": "BS", "style": "nepali"},
    {"name": "Anjali Gurung", "date": "2040-01-05", "cal": "BS", "need": "AD", "style": "full"},
]
 
for c in customers:
    converted = convert_date(c["date"], c["cal"], c["need"], c["style"])
    print(f"{c['name']:<13} | Original: {c['date']} {c['cal']} | Converted: {converted}")
