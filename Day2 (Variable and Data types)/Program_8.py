#Implement a program that converts a given number of
#minutes into hours and minutes


def convert_to_hour(min):
    
    #list to strore minute and hour
    m_list=list()
    
    hour=min//60
    minute=min%60
    
    m_list.append(hour)
    m_list.append(minute)
    
    return m_list


minute=int(input("Enter the minutes: "))

component=convert_to_hour(minute)

print(f"The hour: {component[0]} and minutes: {component[1]}")