def is_gregorian_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False

    return year % 4 == 0

def is_julian_leap_year(year):
    return year % 4 == 0

def is_leap_year(year):
    if year < 1752:
        return is_julian_leap_year(year)

    return is_gregorian_leap_year(year)

# These examples should all print True
print(is_leap_year(1) is False)
print(is_leap_year(2) is False)
print(is_leap_year(3) is False)
print(is_leap_year(4) is True)
print(is_leap_year(1000) is True)
print(is_leap_year(1100) is True)
print(is_leap_year(1200) is True)
print(is_leap_year(1300) is True)
print(is_leap_year(1751) is False)
print(is_leap_year(1752) is True)
print(is_leap_year(1753) is False)
print(is_leap_year(1800) is False)
print(is_leap_year(1900) is False)
print(is_leap_year(2000) is True)
print(is_leap_year(2023) is False)
print(is_leap_year(2024) is True)
print(is_leap_year(2025) is False)
