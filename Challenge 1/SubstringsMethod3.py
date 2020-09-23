import re
def countSubstrings(s, queries):
    
    if s.isalpha() != True or s.islower() != True:
        return 0
    
    result = []
    for i in range(len(queries)):
        if (0 <= queries[i][0], queries[i][1] < len(s)) and queries[i][0] <= queries[i][1]:

            minl = 1
            maxl = queries[i][1] - queries[i][0] + 1

            t = s[queries[i][0]:queries[i][1] + 1]
            out = []
            for i in range(minl,maxl+1):
                p = re.compile('(?=(.{'+str(i)+'}))',re.DOTALL)
                out = out+p.findall(t)

            nodupes = [] 
            k = set() 
            for l in out:
                if l in k:
                    pass
                else:
                    nodupes.append(l)
                    k.add(l)

            result.append(len(nodupes))
        else:
            return 0

    return result
