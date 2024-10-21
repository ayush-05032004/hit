def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def get_month_days(month, year):
    if month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def is_valid_date(day, month, year):
    if month < 1 or month > 12:
        return False
    max_days = get_month_days(month, year)
    if day < 1 or day > max_days:
        return False
    return True

year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

if is_valid_date(day, month, year):
    print("The date", day, "/", month, "/", year, "is valid.")
else:
    print("The date", day, "/", month, "/", year, "is invalid.")