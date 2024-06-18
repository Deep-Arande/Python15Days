# Write a program that converts a given number of days
#into years, weeks, and days


days=int(input("Enter the number of days: "))

years=days//365

weeks=(days%365)//7

day=(days%365)%7

print(f"The number of years: {years}, weeks: {weeks}, days: {day}")