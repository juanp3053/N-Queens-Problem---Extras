# NQueensA_JPG.py
import random

# ask the user for an N value
N = int(input("What Board size do you want? "))
C =0
# generate a candidate NQ solution [random.randint(0,n-1) for x in range(n)]
nq = [random.randint(0,N-1) for x in range(N)]
# define a function to count number of conflicts()
def conflicts(nq):
    c= 0;  
    for i in range(len(nq)-1):
        for j in range(i+1, len(nq)):
            if(((nq[i] == nq[j])) | (abs(nq[i] - nq[j]) == abs(i-j))):
                c+= 1
    return c

#While conflicts arent zero keep shuffling

while(conflicts(nq) != 0 ):  
    nq = [random.randint(0,N-1) for x in range(N)]
    print(nq)
    C += 1
#print winner etc.
print("----------Winner---------")
print(nq)
print(str(C) + " Iterations" )

