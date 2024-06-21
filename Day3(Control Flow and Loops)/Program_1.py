#Create a program that takes a year as input and checks if
#it is a leap year or not


year=int(input("Enter the year: "))

if(year%4==0):
    print(f"The year: {year} is a leap year.")
    
else:
    print(f"The year: {year} is not a leap year.")
    