from itertools import combinations 
def countSubstrings(s, queries):

    if s.isalpha() != True or s.islower() != True:
        return "Invalid"


    result = []
    for i in range(len(queries)):
        if (0 <= queries[i][0], queries[i][1] < n) and queries[i][0] <= queries[i][1]:
            test_str = s[queries[i][0]:queries[i][1] + 1]
            res = [test_str[x:y] for x, y in combinations(range(len(test_str) + 1), r = 2)]

            count = 0
            res2 = []
        
            for j in range(len(res)):
                if res[j] not in res2:
                    res2.append(res[j])
                    count += 1
                else:
                    continue

            result.append(count)
    return result
