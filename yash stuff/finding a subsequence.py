  
import math

        
def biggestSubsequence(arr) : 
    #finding all subsequences
    n = len(arr)
    # Number of subsequences is (2**n -1) 
    opsize = math.pow(2, n) 
    for counter in range( 1, (int)(opsize)) : 
        subseq = []
        for j in range(0, n) :  
            #using bit-shift operation 
            if (counter & (1<<j)) : 
                subseq.append(arr[j])
        print(subseq)
    