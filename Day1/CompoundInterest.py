#Calculate the compound interest for a given principal
#amount, interest rate, and time period


#function which takes amount ,interest rate and time period

def compound_principle(amount,interest,time):
    principle_amount=amount*((1+ interest/100)**time)
    
    return principle_amount-amount


amount=int(input("Enter the amount:"))
interest=float(input("Enter the interest:"))
time=int(input("Enter the number of years:"))

c_interest=compound_principle(amount,interest,time)

print(f"The compound interest is: {c_interest:.3f}")
