import math
import random

trialArray = []
for i in range(5000):
    trialArray.append(random.randint(-10**3, 10**3))

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
        individualSquareSum += arr[i] ** 2
    return int((arraySumSquared - 
            individualSquareSum) / 2)

allArrays = []
"""
def findSubArrays(arr, start, end): 
    # Stop if we have reached the end of the array     
    if end == len(arr): 
        return
    # Increment the end point and start from 0 
    elif start > end: 
        return findSubArrays(arr, 0, end + 1)   
    else: 
        allArrays.append((arr[start:end + 1]))
        return findSubArrays(arr, start + 1, end)
"""
def findSubArrays(arr, n):
    global allArrays 
    # Pick starting point 
    
    for i in range(0,n-1): 
        # Pick ending point 
        for j in range(i+1,n): 
            subArray = []
            # Print subarray between 
            # current starting 
            # and ending points 
            #subArray.append(arr[i:j+1]) 
            for k in range(i,j+1):
                subArray.append(arr[k])
            allArrays.append(subArray)
    

#find a subarray with the highest value      
def largestValue(arr): 
    arrayLength = len(arr)
    if arrayLength <=1 :
        return arr[0]
    largestVal = 0
    findSubArrays(arr,arrayLength)
    for subArray in allArrays:
        newSum = findProductSum(subArray)
        if newSum > largestVal:
            largestVal = newSum
        else:
            continue
    return largestVal

print (largestValue(trialArray))
