import random
"""
testArray = []
for i in range(2*10**5):
    testArray.append(random.randint(0,200))
"""
#print(testArray[34059])
def calculateMedian(arr):
    arr.sort()
    totalLength = len(arr)
    if totalLength%2 == 0:
        median = (arr[totalLength//2-1] + arr[totalLength//2])/2
    else:
        median = arr[totalLength//2]
    return median

def activityNotifications(expenditure, d):
    #initialising all important values
    totalDays = len(expenditure)
    if d == totalDays:
        return 0
    totalChecks = totalDays - d
    totalNotifications = 0
    for i in range(totalChecks):
        #checkArray = []
        requiredData = expenditure[i:i+d]
        dataMedian = calculateMedian(requiredData)
        #print(requiredData, dataMedian,expenditure[i+d], totalNotifications)
        if expenditure[i+d] >= 2*dataMedian:
            print (requiredData, 2*dataMedian, expenditure[i+d])
            totalNotifications += 1
        else:
            pass
    return totalNotifications
"""
f = open("arrayfile.txt",'w')
f.write("1 5000 \n")
writeString = ""
for i in range(5000):
    writeString = writeString + str(testArray[i]) + " "
f.write(writeString)
f.close()
"""
f = open("arrayFile.txt", 'r')
data1 = []
for line in f:
    data1.append(line)
data1[1] = data1[1].split()
for i in range(len(data1[1])):
    data1[1][i] = int(data1[1][i])
    
print(data1)
print(activityNotifications(data1[1],1))

