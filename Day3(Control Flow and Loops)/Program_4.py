#Create a program that generates the Fibonacci sequence
#up to a given number of terms

def Fibonacci(prev_num,cur_num,order,terms):
    
    if(order==terms):
        return
    
    else:
        
        next_num=prev_num+cur_num
        
        print(f"{next_num}",end=' ')
        
        prev_num=cur_num
        cur_num=next_num
        
        Fibonacci(prev_num,cur_num,order+1,terms)
        return
    

terms=int(input("Enter the number of terms to generate fibonacci sequence: "))

print("1",end=' ')
Fibonacci(0,1,1,terms)        


    
    
    

    
