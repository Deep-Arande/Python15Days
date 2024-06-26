# Implement a function to check if a given year is a leap
# year or not


def is_leap_year(year):

    # Check for divisibility by 4
    if year % 4 == 0:
        return True
    else:
        return False  # Leap year if divisible by 4


# Example usage
year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
