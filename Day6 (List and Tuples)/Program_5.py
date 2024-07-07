#Given a list of words, find the word with the maximum
#length and its length


#code

w_list=["Kedar","Ayanish","Shlok","Samartha","Deep","Raj"]

#algo to find word with maximum lenght

max=str(' ')

for i in w_list:
    
    if len(max)<len(i):
        max=i
        

print(f"The word with maximum lenght is {max} and it's lenght is {len(max)}")