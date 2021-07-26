def create_date(month, day, year):
    """Creates a string in date format utilizing 3 inputs for the month, day, and year"""
    returned_date = (month.strip() + "/" + day.strip() + "/" + year.strip())

    return returned_date

def get_date():
    """Get a date from a user with a series of input prompts"""

    #Obtains month from user and validates it
    date_month = input("Please enter the month: ")

    date_ok = False

    while not date_ok:
        date_ok = validate_num(date_month)

        if not date_ok:
            date_month = input("Month was not valid. Please try again: ")
            date_ok = validate_num(date_month)

    #Obtains day from user and validates it
    date_day = input("Please enter the day: ")

    date_ok = False

    while not date_ok:
        date_ok = validate_num(date_day)

        if not date_ok:
            date_day = input("Day was not valid. Please try again: ")
            date_ok = validate_num(date_day)

    #Obtains year from user and validates it
    date_year = input("Please enter the year: ")

    date_ok = False

    while not date_ok:
        date_ok = validate_num(date_year)

        if not date_ok:
            date_month = input("Year was not valid. Please try again: ")
            date_ok = validate_num(date_year)

    #Formats the date
    returned_date = create_date(date_month, date_day, date_year)

    return returned_date

def validate_num(passed_num):
    """Validates whether or not an input is numeric."""

    passed_num = passed_num.strip()

    if passed_num:
        if str(passed_num).isnumeric():
            return True
        else:
            return False
    else:
        return False