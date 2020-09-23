def countSubstrings(s, queries):

    if s.isalpha() != True or s.islower() != True:
        return 0


    result = []
    for i in range(len(queries)):
        parts = []
        if (0 <= queries[i][0], queries[i][1] < n) and queries[i][0] <= queries[i][1]:
            
            minl = 1
            maxl = queries[i][1] - queries[i][0] + 1
 
            t = s[queries[i][0]:queries[i][1] + 1]
            parts = [t[i:i+j] for i in range(len(t)-minl) for j in range(minl,maxl+1)]

            nodupes = [] 
            k = set() 
            for l in parts:
                if l in k:
                    pass
                else:
                    nodupes.append(l)
                    k.add(l)
            result.append(len(nodupes))
    return result
