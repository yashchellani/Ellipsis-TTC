import random
import math

def findProductSum(arr):
    n = len(arr)
    # calculating array sum (a1 + a2 ... + an) 
    arraySum = 0
    for i in range(0, n): 
        arraySum = arraySum + arr[i] 
    arraySumSquared = arraySum ** 2
    # calcualting a1^2 + a2^2 + ... + an^2 
    individualSquareSum = 0
    for i in range(0, n): 
        individualSquareSum += arr[i] * arr[i] 
    return int((arraySumSquared - 
            individualSquareSum) / 2)

#find a subsequence with the highest value      
def largestValue(arr) : 
    largestVal = 0
    #finding all subsequences
    n = len(arr)
    # Number of subsequences is (2**n -1) 
    opsize = math.pow(2, n) 
    for counter in range( 1, (int)(opsize)) : 
        subSeq = []
        for j in range(0, n) :  
            #using bit-shift operation 
            if (counter & (1<<j)) : 
                subSeq.append(arr[j])
            #finding this subseq has the biggest value
            newSum = findProductSum(subSeq)
            
            if newSum > largestVal:
                largestVal = newSum
                print (subSeq, newSum)
            else:
                continue
    return largestVal

print (largestValue([-3,7,-2,3,5,-2]))
