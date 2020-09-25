def solve(arr):
    #proxy for stdin parameter
    arr_count = len(arr) 
    #if arr length is 0 or 1, the only possible subsequence is itself. returns array length+1 if array is already sorted.
    if len(arr) <= 1:
        return arr_count
    #initialising totalIntervals
    totalIntervals = arr_count
    for i in range(arr_count):
        tempList = [arr[i]]
        #print(tempList)
        for j in range (i+1,arr_count):
            if arr[j] >= tempList[-1]:
                totalIntervals += 1
                tempList.append(arr[j])
                print(tempList)
            else:
                break
        tempList = []
        
    return totalIntervals

print(solve([1,2,3,4,5]))
