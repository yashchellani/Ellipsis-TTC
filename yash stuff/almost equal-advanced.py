def findAllPairs(list1):
    pairs = []
    for i in range(len(list1)-1):
        for j in range(i+1, len(list1)):
            pairs.append([list1[i],list1[j]])
    return pairs
print(findAllPairs([1, 3, 4, 3, 0]))

def solve(heights, queries):
    n = len(queries)
    for i in range(n):
        validFights = 0
        heightList = heights[queries[i][0]:queries[i][1]+1]
        fightPairs = findAllPairs(heightList)
        for j in range(len(fightPairs)):
            if abs(fightPairs[i][0]-fightPairs[i][1]) <= k:
                validFights += 1
    return validFights
