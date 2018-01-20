# NQueensC_JPG.py
import random
import math

# ask the user for an N value
N = int(input("What Board size do you want? "))
#Initiation of variables later used.
C =0
S=1
nq = [0] * 4

def genetic(N):
    scores = []
    nq = [0]*4
    genetic = [0]*4
    
    for i in range(0,4):    
        nq[i] = [random.randint(0,N-1) for x in range(N)]
        #print(nq[i])
        #Insert scores in array for further evaluation 
        scores.append(conflicts(nq[i]))
        
    #Look if there is any cero conflicts already
    for i in range(0,4):
        if(scores[i] == 0):
            print("Winner is : " + str(nq[i]))
            return 0;

    #Retain temporary indexes for swapping values, Randomly picked depending on the Conflict score
    temp = scores.index(min(scores))
    temp1 = scores.index(min(n for n in scores if n!=temp))

    #Swap the values between arrays - Preferred to use 1/3 of the most fit list with the 2/3 of the other most fitted list
    genetic[0] = nq[temp][0:(int(N/3))] + nq[temp1][(int(N/3)):(N)]
    genetic[1] = nq[temp1][0:(int(N/3))] + nq[temp][(int(N/3)):(N)]
    #Creates extra random ones - which increases chance of getting the right one
    genetic[2] = [random.randint(0,N-1) for x in range(N)]
    genetic[3] = [random.randint(0,N-1) for x in range(N)]

    #Check for conflicts
    for i in range(0,4):
        if(conflicts(genetic[i]) == 0):
            print("Winner is : " + str(genetic[i]))
            return 0;
        
    print (nq[temp])
    return min(scores);
    
    
#define a function to count number of conflicts()
def conflicts(nq):
    c= 0;  
    for i in range(len(nq)-1):
        for j in range(i+1, len(nq)):
            if(((nq[i] == nq[j])) | (abs(nq[i] - nq[j]) == abs(i-j))):
                c+= 1
    return c

#While conflicts arent zero keep shuffling
print("Keep Waiting, it Might be long... (never give up!)")
for i in range(100000):
    C+=1
    S = genetic(N)
    if(S == 0):
        break;

print(str(C) + " Iterations" )
print(str(S) + " Conflicts" )

