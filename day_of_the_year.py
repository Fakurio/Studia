def is_year_leap(year):
    if (year%4==0 and year%100!=0) or year%400==0:
        return True

def days_in_month(year, month):
    month_days = [31," ",31,30,31,30,31,31,30,31,30,31]
    leap_year = is_year_leap(year)
    if month == 2:
        if leap_year:
            return 29
        else:
            return 28
    else:
        return month_days[month-1]
        
def day_of_year(year, month, day):
    if is_year_leap(year):
        days_in_year = 366
    else:
        days_in_year = 365
    days_passed = 0
    for i in range(1,month):
        days_passed += days_in_month(year,i)
    days_passed += day
    return days_passed

print(day_of_year(2012, 7, 12))
