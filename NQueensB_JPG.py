# NQueensB_JPG0
import random

# ask the user for an N value
N = int(input("What Board size do you want? "))
C =0
# generate a candidate NQ solution 
nq = list(range(N))
random.shuffle(nq)

print(nq)
# define a function to count number of conflicts()
def conflicts(nq):
    c= 0;
    
    for i in range(len(nq)-1):
        for j in range(i+1, len(nq)):
            if(abs(nq[i] - nq[j]) == abs(i-j)):
                c+= 1
    return c
        
#While conflicts arent zero keep shuffling 
while(conflicts(nq) != 0 ):  
    random.shuffle(nq)
    print(nq)
    C += 1
    
#print winner etc.
print("----------Winner---------")
print(nq)
print(str(C) + " Iterations" )



