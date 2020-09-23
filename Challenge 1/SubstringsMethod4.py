def func(s, min_l, max_l):
    return [subl for i in range(min_l, max_l + 1) for subl in map(''.join, zip(*[s[i:] for i in range(i)]))]

def countSubstrings(s, queries):
    
    if s.isalpha() != True or s.islower() != True:
        return 0
    
    result = []
    for i in range(len(queries)):
        if (0 <= queries[i][0], queries[i][1] < len(s)) and queries[i][0] <= queries[i][1]:

            min_l = 1
            max_l = queries[i][1] - queries[i][0] + 1

            t = s[queries[i][0]:queries[i][1] + 1]
            out = func(t, min_l, max_l)

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
