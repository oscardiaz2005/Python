
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def next_date(day, month, year):
    
    days_per_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap_year(year):
        days_per_month[2] = 29

    if 1 <= month <= 12 and 1 <= day <= days_per_month[month]:
     
        if day == days_per_month[month]:
            day = 1
            month += 1
            if month > 12:
                month = 1
                year += 1
        else:
            day += 1
    else:
        print("Invalid date.")
        return None
    
    return day, month, year